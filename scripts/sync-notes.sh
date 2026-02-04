#!/bin/bash

# Sync Obsidian vault to Hugo content/notes
# Syncs Areas/mathematics and Areas/EE, converts wikilinks

VAULT_PATH="/Users/fetzer.jeffrey/repos/jrfwiki"
# Use HUGO_PATH env var if set, otherwise default to parent of script's directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HUGO_PATH="${HUGO_PATH:-$(dirname "$SCRIPT_DIR")}"
NOTES_PATH="$HUGO_PATH/content/notes"
SOURCE_DIRS=("Areas/mathematics" "Areas/electrical_engineering")

# Clean existing notes
rm -rf "$NOTES_PATH"
mkdir -p "$NOTES_PATH"

# Create top-level notes index
cat > "$NOTES_PATH/_index.md" << 'EOF'
---
title: "Notes"
---
EOF

# Temporary file for note mappings
MAPPING_FILE=$(mktemp)

echo "Building note index..."

# First pass: build mapping of note names to URLs
for SOURCE_DIR in "${SOURCE_DIRS[@]}"; do
    find "$VAULT_PATH/$SOURCE_DIR" -name "*.md" -not -path '*/\.*' -not -path '*/lean/*' -not -name "CLAUDE.md" | while read -r file; do
        rel_path="${file#$VAULT_PATH/}"
        url_path="/notes/${rel_path%.md}/"
        filename=$(basename "$file" .md)

        echo "$filename|$url_path" >> "$MAPPING_FILE"
    done
done

echo "Converting notes..."

# Second pass: copy files and convert wikilinks
for SOURCE_DIR in "${SOURCE_DIRS[@]}"; do
    find "$VAULT_PATH/$SOURCE_DIR" -name "*.md" -not -path '*/\.*' -not -path '*/lean/*' -not -name "CLAUDE.md" | while read -r file; do
        rel_path="${file#$VAULT_PATH/}"
        target_dir="$NOTES_PATH/$(dirname "$rel_path")"
        mkdir -p "$target_dir"

        filename=$(basename "$file" .md)
        title="${filename//_/ }"
        target_file="$NOTES_PATH/$rel_path"

        # Rename Index.md to _index.md for Hugo section pages
        if [ "$filename" = "Index" ]; then
            target_file="$(dirname "$target_file")/_index.md"
            # Extract title from first # heading instead of using "Index"
            heading=$(grep -m1 '^# ' "$file" | sed 's/^# //')
            if [ -n "$heading" ]; then
                title="$heading"
            fi
        fi

        # Get relative directory for image path conversion
        note_rel_dir=$(dirname "$rel_path")

        # Process note with Python script
        python3 "$SCRIPT_DIR/process_note.py" "$file" "$MAPPING_FILE" "$title" "$note_rel_dir" > "$target_file"

        echo "Synced: $rel_path"
    done
done

rm -f "$MAPPING_FILE"

# Copy images
IMAGES_PATH="$HUGO_PATH/static/images/notes"
rm -rf "$IMAGES_PATH"
mkdir -p "$IMAGES_PATH"

echo "Copying images..."

for SOURCE_DIR in "${SOURCE_DIRS[@]}"; do
    find "$VAULT_PATH/$SOURCE_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" -o -iname "*.svg" -o -iname "*.webp" \) -not -path '*/\.*' -not -path '*/lean/*' | while read -r file; do
        rel_path="${file#$VAULT_PATH/$SOURCE_DIR/}"
        target_dir="$IMAGES_PATH/$SOURCE_DIR/$(dirname "$rel_path")"
        mkdir -p "$target_dir"
        cp "$file" "$target_dir/"
        echo "Copied: $SOURCE_DIR/$rel_path"
    done
done

image_count=$(find "$IMAGES_PATH" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" -o -iname "*.svg" -o -iname "*.webp" \) 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "Sync complete! $(find "$NOTES_PATH" -name "*.md" | wc -l | tr -d ' ') notes and $image_count images synced."

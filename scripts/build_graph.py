#!/usr/bin/env python3
"""
Build a graph.json file from markdown notes for D3.js visualization.
Scans content/notes/ for markdown files and extracts internal links.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

CONTENT_DIR = Path(__file__).parent.parent / "content" / "notes"
OUTPUT_FILE = Path(__file__).parent.parent / "static" / "graph.json"

def get_title_from_frontmatter(content: str, fallback: str) -> str:
    """Extract title from YAML frontmatter, or use fallback."""
    # Match quoted titles (handles apostrophes inside)
    match = re.search(r'^---\s*\n.*?^title:\s*"([^"\n]+)"\s*$.*?^---',
                      content, re.MULTILINE | re.DOTALL)
    if not match:
        match = re.search(r"^---\s*\n.*?^title:\s*'([^'\n]+)'\s*$.*?^---",
                          content, re.MULTILINE | re.DOTALL)
    if not match:
        # Unquoted title (no quotes or apostrophes)
        match = re.search(r'^---\s*\n.*?^title:\s*([^\n]+?)\s*$.*?^---',
                          content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return fallback.replace("_", " ").replace("-", " ").title()

def extract_category(filepath: Path, content_dir: Path) -> str:
    """Extract category from file path.

    Strategy:
    - For paths containing 'definitions/' -> use parent of definitions (TopicName)
    - For paths containing 'books/' -> Books
    - For topic files like TopicName/TopicName.md -> use TopicName
    - Otherwise -> Uncategorized
    """
    rel_path = filepath.relative_to(content_dir)
    parts = [p.lower() for p in rel_path.parts]
    original_parts = rel_path.parts

    # Check for definitions pattern: TopicName/definitions/file.md
    if "definitions" in parts:
        idx = parts.index("definitions")
        if idx > 0:
            return original_parts[idx - 1]

    # Check for books directory - use the topic (parent of books)
    if "books" in parts:
        idx = parts.index("books")
        if idx > 0:
            return original_parts[idx - 1]
        return "Books"

    # For topic files like mathematics/TopicName/TopicName.md or
    # electrical_engineering/TopicName/TopicName.md
    # The topic is the parent directory
    if len(original_parts) >= 3:
        # Path structure: Area/TopicName/File.md
        area = parts[1] if len(parts) > 1 else None
        if area and filepath.stem.lower() != 'index' and not filepath.stem.startswith('_'):
            # Return the topic directory name (second-to-last component)
            return original_parts[-2]

    return "Uncategorized"

def extract_links(content: str) -> list[str]:
    """Extract internal note links from markdown content."""
    # Match markdown links like [text](/notes/path/to/note/)
    pattern = r'\[([^\]]*)\]\((/notes/[^)]+)\)'
    matches = re.findall(pattern, content)
    return [url.rstrip('/').lower() for _, url in matches]

def path_to_url(filepath: Path, content_dir: Path) -> str:
    """Convert a file path to its URL path."""
    rel_path = filepath.relative_to(content_dir.parent)
    # Remove .md extension and convert to URL
    # Also remove apostrophes to match Hugo's URL generation
    url = "/" + str(rel_path.with_suffix("")).lower().replace("'", "")
    return url

def build_graph():
    """Build the graph data structure from markdown files."""
    nodes = {}  # url -> {id, title, path, category}
    edges = []  # [{source, target}]

    # First pass: collect all notes as nodes with categories
    for md_file in CONTENT_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue

        url = path_to_url(md_file, CONTENT_DIR)
        content = md_file.read_text(encoding="utf-8")
        title = get_title_from_frontmatter(content, md_file.stem)
        category = extract_category(md_file, CONTENT_DIR)

        nodes[url] = {
            "id": url,
            "title": title,
            "path": str(md_file.relative_to(CONTENT_DIR)),
            "category": category,
        }

    # Second pass: extract links and build edges
    for md_file in CONTENT_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue

        source_url = path_to_url(md_file, CONTENT_DIR)
        content = md_file.read_text(encoding="utf-8")
        links = extract_links(content)

        for target_url in links:
            # Only add edge if target exists in our nodes
            if target_url in nodes:
                edges.append({
                    "source": source_url,
                    "target": target_url,
                })

    # Third pass: compute backlinks (what links TO each note)
    backlinks = defaultdict(list)
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        # Add source to the list of backlinks for target
        if source not in backlinks[target]:
            backlinks[target].append(source)

    return {
        "nodes": list(nodes.values()),
        "edges": edges,
        "backlinks": dict(backlinks),
    }

def main():
    print(f"Scanning {CONTENT_DIR} for markdown files...")

    graph = build_graph()

    print(f"Found {len(graph['nodes'])} notes and {len(graph['edges'])} links")

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    print(f"Wrote graph data to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

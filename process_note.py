#!/usr/bin/env python3
"""Process Obsidian markdown for Hugo - wikilink conversion and math fixes."""

import re
import sys


def load_mapping(mapping_file):
    """Load note name to URL mapping."""
    mapping = {}
    with open(mapping_file, 'r') as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                name, url = line.split('|', 1)
                mapping[name] = url
    return mapping


def hugo_url(url):
    """Convert URL to match Hugo's URL sanitization."""
    if not url:
        return url
    # Hugo lowercases and removes apostrophes
    url = url.lower()
    url = url.replace("'", "")
    return url


def convert_wikilinks(content, mapping):
    """Convert [[wikilinks]] to markdown links."""
    # [[target|display]] format
    def replace_aliased(match):
        target = match.group(1)
        display = match.group(2)
        target = re.sub(r'\.md$', '', target)
        target = target.split('/')[-1]
        url = mapping.get(target)
        return f'[{display}]({hugo_url(url)})' if url else display

    content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', replace_aliased, content)

    # [[target]] format
    def replace_simple(match):
        target = match.group(1)
        display = target
        target = re.sub(r'\.md$', '', target)
        target = target.split('/')[-1]
        url = mapping.get(target)
        return f'[{display}]({hugo_url(url)})' if url else display

    content = re.sub(r'\[\[([^\]]+)\]\]', replace_simple, content)

    return content


def fix_math_blocks(content):
    """Fix math blocks for Hugo/Goldmark.

    Issues handled:
    1. Lines starting with " - " inside math get parsed as lists
    2. Lines starting with "> " inside math come from blockquotes
    3. Display math should have $$ on own lines
    4. Blockquotes followed by math need blank line separation
    """
    def fix_display_math(match):
        inner = match.group(1).strip()

        # Fix the " - x" list issue by removing space between \\ and -
        inner = re.sub(r'\\\\\s*\n\s*-', r'\\\\ -', inner)

        # Remove blockquote markers from inside math
        lines = inner.split('\n')
        fixed_lines = []
        for line in lines:
            # Strip leading > from blockquotes
            line = re.sub(r'^>\s*', '', line)
            # Handle lines starting with -
            stripped = line.lstrip()
            if stripped.startswith('-') and not stripped.startswith('-\\'):
                indent = len(line) - len(stripped)
                line = ' ' * indent + '\\text{-}' + stripped[1:]
            fixed_lines.append(line)
        inner = '\n'.join(fixed_lines)

        # Put $$ on their own lines for proper block rendering
        return '\n\n$$\n' + inner + '\n$$\n\n'

    # Match $$...$$ blocks (multiline)
    content = re.sub(r'\$\$(.*?)\$\$', fix_display_math, content, flags=re.DOTALL)

    # Ensure blockquotes are separated from following math blocks
    # Pattern: line starting with > followed by newlines then $$
    content = re.sub(r'(^>.*?)\n+(\$\$)', r'\1\n\n\2', content, flags=re.MULTILINE)

    return content


def add_frontmatter(content, title):
    """Add Hugo frontmatter if missing."""
    if content.startswith('---\n'):
        return content
    return f'---\ntitle: "{title}"\n---\n\n{content}'


def process_note(input_file, mapping_file, title):
    """Process a single note file."""
    mapping = load_mapping(mapping_file)

    with open(input_file, 'r') as f:
        content = f.read()

    content = convert_wikilinks(content, mapping)
    content = fix_math_blocks(content)
    content = add_frontmatter(content, title)

    print(content, end='')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <input_file> <mapping_file> <title>', file=sys.stderr)
        sys.exit(1)

    process_note(sys.argv[1], sys.argv[2], sys.argv[3])

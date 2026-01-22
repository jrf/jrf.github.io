#!/usr/bin/env python3
"""
Build a graph.json file from markdown notes for D3.js visualization.
Scans content/notes/ for markdown files and extracts internal links.
"""

import os
import re
import json
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content" / "notes"
OUTPUT_FILE = Path(__file__).parent.parent / "static" / "graph.json"

def get_title_from_frontmatter(content: str, fallback: str) -> str:
    """Extract title from YAML frontmatter, or use fallback."""
    match = re.search(r'^---\s*\n.*?^title:\s*["\']?([^"\'\n]+)["\']?\s*$.*?^---',
                      content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return fallback.replace("_", " ").replace("-", " ").title()

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
    url = "/" + str(rel_path.with_suffix("")).lower()
    return url

def build_graph():
    """Build the graph data structure from markdown files."""
    nodes = {}  # url -> {id, title, path}
    edges = []  # [{source, target}]

    # First pass: collect all notes as nodes
    for md_file in CONTENT_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue

        url = path_to_url(md_file, CONTENT_DIR)
        content = md_file.read_text(encoding="utf-8")
        title = get_title_from_frontmatter(content, md_file.stem)

        nodes[url] = {
            "id": url,
            "title": title,
            "path": str(md_file.relative_to(CONTENT_DIR)),
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

    return {
        "nodes": list(nodes.values()),
        "edges": edges,
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

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website built with Hugo and the PaperMod theme. Hosted on GitHub Pages at jrf.io.

## Build and Development Commands

Use `just` for all common operations:

```bash
just serve      # Local dev server with live reload
just drafts     # Serve including draft posts
just build      # Production build (outputs to public/)
just clean      # Remove public/ directory
just new "title"     # Create new post
just new-page "path" # Create new page
```

### Notes Pipeline

Notes are synced from an Obsidian vault (~/repos/jrfwiki):

```bash
just sync       # Sync notes from Obsidian vault
just graph      # Build graph.json for visualization
just sync-all   # Sync notes and rebuild graph
```

The sync pipeline:
1. `scripts/sync-notes.sh` - Copies markdown from `Areas/mathematics` and `Areas/electrical_engineering` in the vault
2. `scripts/process_note.py` - Converts Obsidian wikilinks to Hugo markdown links, fixes math blocks, converts callouts
3. `scripts/build_graph.py` - Generates `static/graph.json` for the D3.js knowledge graph

## Content Structure

- `content/posts/` - Blog posts (shown on homepage)
- `content/notes/` - Synced from Obsidian vault (do not edit directly, changes will be overwritten)
- `content/graph/` - Interactive D3.js knowledge graph visualization
- `content/code/` - Code examples

## Key Configuration

- `hugo.toml` - Site config. Math enabled via Goldmark passthrough for `$...$` and `$$...$$`
- Theme: PaperMod (in `themes/PaperMod/`)
- Hugo version: 0.147.0 (specified in `.github/workflows/hugo.yml`)

## Custom Layouts

- `layouts/graph/single.html` - Full-page D3.js knowledge graph with search, category filtering, and slide-out panel
- `layouts/partials/local-graph.html` - Per-note mini graph showing connected notes
- `layouts/partials/backlinks.html` - Shows which notes link to the current note
- `layouts/notes/` - Custom templates for note pages

## Deployment

Automatic via GitHub Actions on push to main. Workflow in `.github/workflows/hugo.yml` builds and deploys to GitHub Pages.

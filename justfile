# Default recipe - list available commands
default:
    @just --list

# Serve the site locally with live reload
serve:
    hugo server

# Serve the site including draft posts
drafts:
    hugo server -D

# Serve the site including future-dated posts
future:
    hugo server -F

# Serve with drafts, future posts, and expired content
all:
    hugo server -D -F -E

# Build the site for production
build:
    hugo --minify

# Build including drafts (for preview)
build-drafts:
    hugo -D --minify

# Clean the public directory
clean:
    rm -rf public

# Create a new post (usage: just new "my-post-title")
new title:
    hugo new content posts/{{title}}.md

# Create a new page
new-page title:
    hugo new content {{title}}.md

# Build and serve the production build locally
preview: build
    cd public && python3 -m http.server 8000

# Check for broken links (requires htmltest)
check: build
    htmltest

# Watch for changes and rebuild (without serving)
watch:
    hugo --watch

.PHONY: install build serve clean

# Install dependencies
install:
	gem install bundler
	bundle install

# Build the site
build:
	bundle exec jekyll build

# Serve locally with live reload
serve:
	bundle exec jekyll serve

# Clean built files
clean:
	bundle exec jekyll clean
	rm -rf _site .jekyll-cache

# Start fresh - clean everything and reinstall
fresh: clean
	rm -rf vendor
	rm -f Gemfile.lock
	make install

# Initialize a new Jekyll site
init:
	jekyll new .

# Update gems
update:
	bundle update

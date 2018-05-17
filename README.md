### Description

My personal site

#### Install


	bundle update
	bundle install
	npm install
	sudo npm install -g grunt grunt-cli

#### Build
Run

	grunt watch
	bundle exec jekyll serve --watch --host 0.0.0.0

Generates to `_site`. All `_` prefixed folders are ignored in generation.
Can use `--limit_posts 1` in conjunction with `jekyll serve`. Can use `--incremental`

`grunt-jekyll` no longer works because the latest jekyll is not supported by this grunt plugin.


# [David Alberto Adler](https://davidalbertoadler.com)

## About

Source code for [personal site of David Alberto Adler](https://davidalbertoadler.com). A calling card and a place to aggregate my projects.


### Install


	bundle update
	bundle install
	npm install
	sudo npm install -g grunt grunt-cli

#### Develop

Run

	grunt watch
	bundle exec jekyll serve --watch --host 0.0.0.0

- Generates to `_site`. 
- All `_` prefixed folders are ignored in generation.
- Can use `--limit_posts 1` in conjunction with `jekyll serve`. Can use `--incremental`


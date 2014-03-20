---
layout: post
title:  "Hello blog, hello jekyll, hello world!"
date:   2014-03-19 15:30:27
categories: jekyll update
---

Here is my first ever blog post. This blog is powered by: [jekyll](http://jekyllrb.com/), [github pages](http://pages.github.com/), [disqus](http://disqus.com/), [grunt](http://gruntjs.com/) and [jade](http://jade-lang.com/). Why not start this blog with a tutorial of how I made this blog:

1. **To create a github page:** sign in to github, create a repo `my_username.github.io`. What ever you put in here will be live at [http://my_username.github.io](http://my_username.github.io)
2. **Install jekyll:** Once cloned in the repo do 

        gem install bundler
        printf "source 'https://rubygems.org'\ngem 'github-pages'" > Gemfile 
        bundle install
NB requires `ruby 1.9.1` or `2.0.0`, full instructions here
3. **Run jekyll:** with `bundle exec jekyll serve`
4. **Grunt:** for livereload, jade compiling and in the future much more great stuff. First you need to *create* a `package.json` with the following contents:

        {
          "name": "blog",
          "version": "0.0.1",
          "private": true,
          "devDependencies": {
            "grunt": "^0.4.4",
            "grunt-contrib-watch": "^0.6.1",
            "grunt-jekyll": "^0.4.1",
            "grunt-contrib-jade": "^0.11.0",
            "grunt-concurrent": "^0.5.0"
          }
        }
Then create a `Gruntfile.js` with the following contents:

        module.exports = function(grunt) {

            // Project configuration.
            grunt.initConfig({
                pkg: grunt.file.readJSON('package.json'),
                src: {
                    html: ['_layouts/*.html', 'index.html'],
                    css: ['css/*'],
                    other: ['projects/*'],
                    posts: ['_posts/*', '_drafts/*']
                },
                jekyll: { 
                    options: {bundleExec: true },
                    dist: {options: {config: '_config.yml'} },
                    serve: { 
                        options: {
                            drafts: true,
                            watch: true,
                            serve : true
                        }
                    }
                },
                watch: {
                    files: ['<%= src.posts %>'],
                    tasks: ['jade'],
                    options: {livereload: {port: 12345 } }
                },
                jade: {
                  compile: {
                    options: {
                      data: {
                                debug: false
                            }
                        },
                        files: {
                            "_layouts/default.html": "_layouts/jade/default.jade",
                            "_layouts/post.html": "_layouts/jade/post.jade"
                        }
                    }
                },
                concurrent: {
                    target: {
                        tasks: ['jekyll:serve', 'watch'],
                        options: {logConcurrentOutput: true } }
            }

            });
               
            // Default task(s).
            grunt.registerTask('default', ['jade', 'concurrent:target']);


            // Load the plugin that provides the "uglify" task.
            grunt.loadNpmTasks('grunt-jekyll');
            grunt.loadNpmTasks('grunt-concurrent');
            grunt.loadNpmTasks('grunt-contrib-watch');
            grunt.loadNpmTasks('grunt-contrib-jade');

        };
Then install grunt with:

        sudo npm install -g grunt-cli
        sudo npm install
Then run grunt with 

        grunt
5. **Jade:** I've converted the `default.html` and `post.html` into [`default.jade`]({{ site.url }}/assets/default.jade) and [`post.jade`]({{ site.url }}/assets/post.jade). Move these into `_layouts/jade`.
6. **Disqus comments:** Register with disqus and add this to the bottom of `post.jade`.
    
        div#disqus_thread
            script(type='text/javascript')
                |  /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
                |  var disqus_shortname = 'MY_USERNAME'; // required: replace example with your forum shortname
                |  /* * * DON'T EDIT BELOW THIS LINE * * */
                |  (function() {
                |  var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                |  dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                |  (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                |  })();
            noscript
              | Please enable JavaScript to view the
              a(href='http://disqus.com/?ref_noscript') comments powered by Disqus.
            a.dsq-brlink(href='http://disqus.com')
              | comments powered by
              span.logo-disqus Disqus
        {% if page.comments %}
        {% endif %}
Make sure you replace `MY_USERNAME` with you're actual disqus username. Add `comments: true` to the top of `post.jade`
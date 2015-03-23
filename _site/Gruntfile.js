module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        src: {
            html: [
                '_layouts/*.html',
                'index.html'
            ],
            css: [
                'css/*'
            ],
            other: [
                '_layouts/jade/*.jade',
                'projects/*.jade',
                'cv/pt/index.jade'
            ],
            posts: [
                '_posts/*',
                '_posts/*.markdown',
                '_drafts/*'
            ]
        },
        jekyll: {
            options: {
                bundleExec: true
            },
            dist: {
                options: {
                    config: '_config.yml'
                }
            },
            build: {
                options: {
                    drafts: false
                }
            },
            serve: {
                options: {
                    drafts: true,
                    watch: true,
                    serve: true
                }
            }
        },
        jade: {
            compile: {
                options: {
                    data: {
                        debug: false
                    }
                },
                files: {
                    "cv/pt/index.html": "cv/pt/index.jade",
                    "projects/index.html": "projects/index.jade",
                    "_layouts/default.html": "_layouts/jade/default.jade",
                    "_layouts/post.html": "_layouts/jade/post.jade"
                }
            }
        },
        concurrent: {
            target: {
                tasks: ['jekyll:serve', 'watch'],
                options: {
                    logConcurrentOutput: true
                }
            }
        },
        watch: {
            files: ['<%= src.posts %>', '<%= src.other %>', 'Gruntfile.js'],
            tasks: ['jade'],
            options: {
                livereload: {
                    port: 12345
                }
            }
        }

    });

    // Default task(s).
    grunt.registerTask('default', ['jade', 'jekyll:build', 'concurrent:target']);
    grunt.registerTask('watch', ['watch']);


    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-jekyll');
    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jade');
    // grunt.loadNpmTasks('grunt-contrib-concat');
    // grunt.loadNpmTasks('grunt-contrib-uglify');
    // grunt.loadNpmTasks('grunt-contrib-jshint');

};

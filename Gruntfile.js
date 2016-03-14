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
        sass: {
          dist: {
            files: {
              'css/main.css': 'scss/main.scss',
              'landing-page-src/styles.css': 'landing-page-src/scss/styles.scss'
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
        concat: {
            options: {
                separator: ';',
            },
            dist: {
                src: ['assets/js/jquery-1.9.1.min.js', 'assets/js/typed.js'],
                dest: 'assets/js/landing-page-libs.min.js',
            },
        },
        includes: {
          files: {
            src: [
                'landing-page-src/index.html',
                'landing-page-src/html5up.html',
                'landing-page-src/styles.html'
            ],
            dest: 'hi', // Destination directory
            flatten: true,
            cwd: '.',
            options: {
              silent: false
            }
          }
        },
        watch: {
            files: ['scss/*', '<%= src.other %>', '<%= src.posts %>', 'landing-page-src/**'],
            tasks: ['jade', 'sass', 'includes'],
            options: {
                livereload: {
                    port: 12345
                }
            }
        }

    });

    // Default task(s).
    grunt.registerTask('default', ['jade', 'sass', 'concat', 'includes', 'watch']);
    grunt.registerTask('watch', ['watch']);
    grunt.registerTask('include', ['includes']);


    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-jekyll');
    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jade');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-includes');
    // grunt.loadNpmTasks('grunt-contrib-uglify');
    // grunt.loadNpmTasks('grunt-contrib-jshint');

};

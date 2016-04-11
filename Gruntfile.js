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
                '_cv/pt/index.jade'
            ],
            posts: [
                '_posts/*',
                '_posts/*.markdown',
                '_drafts/*'
            ]
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
        sass: {
          dist: {
            files: {
              'css/main.css': '_scss/main.scss',
              'css/landing-page.css': '_landing-page-src/scss/styles.scss'
            }
          }
        },
        includes: {
          files: {
            src: [
                '_landing-page-src/index.html'
            ],
            dest: '_layouts', // Destination directory
            flatten: true,
            cwd: '.',
            options: {
              silent: false
            }
          }
        },
        watch: {
            files: ['_scss/*', '<%= src.other %>', '<%= src.posts %>', '_landing-page-src/**'],
            tasks: ['includes'],
            options: {
                livereload: {
                    port: 12345
                }
            }
        }

    });

    // Default task(s).
    grunt.registerTask('default', ['sass', 'includes', 'watch']);
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

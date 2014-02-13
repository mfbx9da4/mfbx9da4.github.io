module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        jshint: {
            // define the files to lint
            files: ['../main.js','../Gruntfile.js'],
            // configure JSHint (documented at http://www.jshint.com/docs/)
            options: {
                // more options here if you want to override JSHint defaults
                globals: {
                    jQuery: true,
                    console: true,
                    module: true
                }
            }
        },
        watch: {
            files: ['<%= jshint.files %>', '../index.html', '../main.css'],
            tasks: ['jshint'],
            options: {
                livereload: {
                    port: 12345
                }
            }
        }

    });
       
    // Default task(s).
    grunt.registerTask('default', ['watch']);


    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jshint');

};
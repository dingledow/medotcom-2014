fs = require 'fs'

module.exports = (grunt) ->

    grunt.initConfig {
        ASSETS:         'srv/assets/'

        SRC_SCSS:       '<%= ASSETS %>scss/'

        # sass
        sass: {
            options: {
                style: 'compressed'
            }
            dist: {
                files: {
                    'srv/static/css/global.css': '<%= SRC_SCSS %>global.scss'
                }
            }
        }

        # Do collectstatic
        shell: {
          collectstatic: {
            options: {
              stdout: true
            }
            command: 'python app/manage.py collectstatic --noinput --settings=app.settings.local'
          }
        }

        # watch files for development
        watch: {
            scss: {
                files: ['<%= SRC_SCSS %>*.scss']
                tasks: ['build']
            }
        }
    }

    # load the tasks
    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-contrib-sass'
    grunt.loadNpmTasks 'grunt-shell'

    # register tasks
    grunt.registerTask 'build',
        'All build tasks',
        ['sass', 'shell']

    # info on watch event
    grunt.event.on 'watch', (action, filepath) ->
        grunt.log.writeln "#{filepath} has #{action}"

gulp = require 'gulp'
gutil = require 'gulp-util'
gulpif = require 'gulp-if'
concat = require 'gulp-concat'
sourcemaps = require 'gulp-sourcemaps'

sass = require 'gulp-sass'

coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'

browserSync = require 'browser-sync'

PROJECT = 'ebisc'
DJANGO = '127.0.0.1:8000'

# -----------------------------------------------------------------------------
# Styles

STYLES =
    main: 'assets/styles/main.scss'
    admin: 'assets/styles/admin.scss'

processStyles = (src) ->
    gulp.src src
        .pipe sourcemaps.init()
        .pipe sass
            errLogToConsole: true
        .on('error', onError)
        .pipe sourcemaps.write 'maps'
        .pipe gulp.dest "#{PROJECT}/static/styles/"
        .pipe browserSync.reload
            stream: true

gulp.task 'styles', [], () ->
    processStyles STYLES.main
    processStyles STYLES.admin

# -----------------------------------------------------------------------------
# Scripts

SCRIPTS =
    main: 'assets/scripts/components/collapsible-menu.coffee'

processScripts = (src, target) ->
    console.log "#{PROJECT}/static/scripts/#{target}"
    gulp.src src
        .pipe sourcemaps.init()
        .pipe gulpif /[.]coffee$/, coffee()
        .pipe concat target
        .pipe uglify()
        .pipe sourcemaps.write 'maps'
        .pipe gulp.dest "#{PROJECT}/static/scripts/"
        .pipe browserSync.reload
            stream: true

gulp.task 'scripts', [], () ->
    processScripts SCRIPTS.main, 'main.js'

# -----------------------------------------------------------------------------
# Build

gulp.task 'build', ['styles', 'scripts'], () ->
    return

# -----------------------------------------------------------------------------
# Default - watch & sync

gulp.task 'default', () ->

    browserSync
        notify: false
        proxy: DJANGO

    gulp.watch(['assets/**/*.coffee', 'assets/**/*.scss'], ['scripts', 'styles'])
    gulp.watch(["#{PROJECT}/**/*.py", "#{PROJECT}/**/*.html"]).on('change', browserSync.reload);

# -----------------------------------------------------------------------------
# Utils

onError = (error) ->
    gutil.beep()
    gutil.log gutil.colors.red('Error'), error.message

# -----------------------------------------------------------------------------

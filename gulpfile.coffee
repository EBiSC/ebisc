gulp = require 'gulp'
gutil = require 'gulp-util'
gulpif = require 'gulp-if'
concat = require 'gulp-concat'
rename = require 'gulp-rename'

sourcemaps = require 'gulp-sourcemaps'

sass = require 'gulp-sass'

coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'
browserify = require 'gulp-browserify'

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
    main: [
        'assets/scripts/components/dropdown.coffee'
        'assets/scripts/components/collapsible-menu.coffee'
    ]

processScripts = (src, target) ->
    gulp.src src
        .pipe sourcemaps.init()
        .pipe gulpif /[.]coffee$/, coffee()
        .on('error', onError)
        .pipe concat target
        .pipe uglify()
        .pipe sourcemaps.write 'maps'
        .pipe gulp.dest "#{PROJECT}/static/scripts/"
        .pipe browserSync.reload
            stream: true

gulp.task 'scripts', [], () ->
    processScripts SCRIPTS.main, 'main.js'

# -----------------------------------------------------------------------------
# REACT Apps

REACT_APPS = [
    ['assets/scripts/search/main.cjsx', 'search.js']
]

buildReactApp = (src, target) ->
    gulp.src src, read: false
        .pipe browserify
            transform: ['coffee-reactify']
            extensions: ['.cjsx']
            debug: true
        .on('error', onError)
        .pipe sourcemaps.init()
        .pipe uglify()
        .pipe sourcemaps.write 'maps'
        .pipe rename target
        .pipe gulp.dest "#{PROJECT}/static/scripts/"
        .pipe browserSync.reload
            stream: true

gulp.task 'react-apps', [], () ->
    for app in REACT_APPS
        buildReactApp app[0], app[1]

# -----------------------------------------------------------------------------
# Build

gulp.task 'build', ['styles', 'scripts', 'react-apps'], () ->
    return

# -----------------------------------------------------------------------------
# Default - watch & sync

gulp.task 'default', () ->

    browserSync
        notify: false
        proxy: DJANGO

    gulp.watch(['assets/**/*.coffee'], ['scripts'])
    gulp.watch(['assets/**/*.scss'], ['styles'])
    gulp.watch(['assets/**/*.cjsx'], ['react-apps'])

    gulp.watch(["#{PROJECT}/**/*.py", "#{PROJECT}/**/*.html"]).on('change', browserSync.reload)

# -----------------------------------------------------------------------------
# Utils

onError = (error) ->
    gutil.beep()
    gutil.log gutil.colors.red('Error'), error.message

# -----------------------------------------------------------------------------

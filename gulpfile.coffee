gulp = require 'gulp'
gutil = require 'gulp-util'
gulpif = require 'gulp-if'
concat = require 'gulp-concat'
source = require('vinyl-source-stream')
buffer = require('vinyl-buffer')

sourcemaps = require 'gulp-sourcemaps'

sass = require 'gulp-sass'

coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'

watchify = require('watchify')
browserify = require 'browserify'

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
        .pipe sourcemaps.write('maps')
        .pipe gulp.dest("#{PROJECT}/static/styles/")
        .pipe browserSync.reload(stream: true)

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
        .pipe concat(target)
        .pipe uglify()
        .pipe sourcemaps.write('maps')
        .pipe gulp.dest("#{PROJECT}/static/scripts/")
        .pipe browserSync.reload(stream: true)

gulp.task 'scripts', [], () ->
    processScripts SCRIPTS.main, 'main.js'

# -----------------------------------------------------------------------------
# Browserify style apps

APPS = [
    ['./assets/scripts/search/main.cjsx', 'search.js']
]

browserifyApp = (src, target, watch=false) ->

    bundle = () ->
        bundler.bundle()
            .on('error', onError)
            .pipe source(target)
                .pipe buffer()
                .pipe sourcemaps.init(loadMaps: true)
                # .pipe uglify()
                .pipe sourcemaps.write('maps')
            .pipe gulp.dest("#{PROJECT}/static/scripts/")
            .pipe browserSync.reload(stream: true)

    if watch
        bundler = watchify(browserify(
            cache: {}
            packageCache: {}
            transform: ['coffee-reactify']
            extensions: ['.cjsx']
        ))

        bundler.on('update', bundle)

    else
        bundler = browserify(
            transform: ['coffee-reactify']
            extensions: ['.cjsx']
        )

    bundler.add(src)
    bundler.on('log', gutil.log)

    bundle()

gulp.task 'apps', [], () ->
    for app in APPS
        browserifyApp(app[0], app[1])

# -----------------------------------------------------------------------------
# Build

gulp.task 'build', ['styles', 'scripts', 'apps'], () ->
    return

# -----------------------------------------------------------------------------
# Default - watch & sync

gulp.task 'default', () ->

    browserSync
        notify: false
        proxy: DJANGO

    gulp.watch(['assets/**/*.coffee'], ['scripts'])
    gulp.watch(['assets/**/*.scss'], ['styles'])

    gulp.watch(["#{PROJECT}/**/*.py", "#{PROJECT}/**/*.html"]).on('change', browserSync.reload)

    for app in APPS
        browserifyApp(app[0], app[1], true)

# -----------------------------------------------------------------------------
# Utils

onError = (error) ->
    gutil.beep()
    gutil.log gutil.colors.red('Error'), error.message

# -----------------------------------------------------------------------------

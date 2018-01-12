'use strict';

var gulp = require('gulp');
var path = require('path');
var gutil = require('gulp-util');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');

var _ = require('lodash');
var nodeResolve = require('resolve');

var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');

var sass = require('gulp-sass');

var browserify = require('browserify');
var watchify = require('watchify');
var coffeeReactify = require('coffee-reactify')
// var babelify = require('babelify');

var browserSync = require('browser-sync').create();

var DJANGO = '127.0.0.1:8000';

// ----------------------------------------------------------------------------
// Definitionas

var PROJECT = 'ebisc';
var PROJECT_STATIC = path.join(PROJECT, 'static');

var STYLES = [
    'assets/styles/main.scss',
    'assets/styles/admin.scss',
]

var SCRIPTS = [
  {
    target: 'search.js',
    entry: 'assets/scripts/search/main.cjsx',
    vendor: ''
  },
  {
    target: 'main.js',
    entry: 'assets/scripts/main.coffee',
  },
]

// ----------------------------------------------------------------------------
// Default

gulp.task('default', ['styles', 'scripts-watch'], function() {

  browserSync.init({
    notify: false,
    proxy: DJANGO,
    open: false,
  });

  gulp.watch(['assets/**/*.scss'], ['styles']);
  gulp.watch([path.join(PROJECT, '**/*.html')])
    .on('change', browserSync.reload);
});

// ----------------------------------------------------------------------------
// Build

gulp.task('build', ['styles', 'scripts']);

// ----------------------------------------------------------------------------
// Styles

function processStyle(src) {
  gulp.src(src)
    .pipe(sourcemaps.init())
    .pipe(sass({outputStyle: 'compressed'}))
    .on('error', handleError)
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(path.join(PROJECT_STATIC, 'styles')))
    .pipe(browserSync.stream({match: '**/*.css'}));
}

gulp.task('styles', [], function () {
  _.forEach(STYLES, function (style) {
    processStyle(style);
  });
});

// ----------------------------------------------------------------------------
// Scripts

gulp.task('scripts', [], function () {
  createScriptBundles(false);
});

gulp.task('scripts-watch', [], function () {
  createScriptBundles(true)
});

function createScriptBundles(watch) {
  for (var i in SCRIPTS) {
    createScriptBundle(SCRIPTS[i], watch)
  }
}

function createScriptBundle(item, watch) {

  var options = {
    debug: true,
    cache: {},
    packageCache: {},
    extensions: ['.coffee', '.cjsx'],
  }

  var bundler = browserify(item.entry, options)
    .transform(coffeeReactify);

  if (watch) {
    bundler = watchify(bundler)
      .on('log', gutil.log)
      .on('update', bundle);
  }

  function bundle() {
    bundler.bundle()
      .on('error', handleError)
      .pipe(source(item.target))
      .pipe(buffer())
      .pipe(sourcemaps.init({loadMaps: true}))
      .pipe(uglify())
      .pipe(sourcemaps.write('.'))
      .pipe(gulp.dest(path.join(PROJECT_STATIC, 'scripts')))
      .pipe(browserSync.stream({match: '**/*.js'}));
  }

  return bundle();
}

// ----------------------------------------------------------------------------
// Utils

var handleError = function(error) {
    gutil.beep();
    gutil.log(gutil.colors.red('Error'), error.message);
    this.emit('end');
};

// ----------------------------------------------------------------------------

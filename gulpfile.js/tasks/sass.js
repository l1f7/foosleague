/**
 * Stylus
 * ----------------------------------------------------
 * Super terse css preprocessor awesomeness
 */

var gulp         = require('gulp')
,   bs           = require('browser-sync')
,   sass         = require('gulp-sass')
,   srcmaps      = require('gulp-sourcemaps')
,   handleErrors = require('../lib/handleErrors')
,   config       = require('../config/sass')
,   autoprefixer = require('gulp-autoprefixer');

gulp.task('sass', function () {
  return gulp.src(config.src)
    .pipe(srcmaps.init())
    .pipe(sass(config.settings))
    .on('error', handleErrors)
    .pipe(autoprefixer())
    .pipe(srcmaps.write('./maps'))
    .pipe(gulp.dest(config.dest))
    .pipe(bs.reload({stream:true}));
});
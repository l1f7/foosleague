/**
 * Browsersync
 * ----------------------------------------------------
 * Make it easy and fast to develop in the browser
 */
var browserSync = require('browser-sync');
var gulp        = require('gulp');
var config      = require('../config/browserSync')

gulp.task('browserSync', function() {
  return browserSync(config);
});

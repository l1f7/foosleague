/**
 * This is the file where we configure all the top-level
 * tasks that our build processes use.
 */

var gulp      = require('gulp')
,   beep      = require('beepbeep')
,   sequence  = require('gulp-sequence')
,   notifier  = require('gulp-notify/node_modules/node-notifier')
,   gutil     = require('gulp-util')
,   argv      = require('yargs').argv;

// We get an error by running "gulp" alone without
// a default task assigned, so we're just covering
// our bases here
gulp.task('default', function (cb) {

  if (argv.proto) {             // gulp --proto
    sequence('prototype', cb);
  } else if (argv.dev) {        // gulp --dev
    sequence('development', cb);
  } else if (argv.prod) {       // gulp --prod
    sequence('production', cb);
    beep(2);
    notifier.notify({
      'title': 'Gulp Error',
      'subtitle': 'Running Production tasks',
      'message': 'Are you sure you want to be running production tasks manually?'
    });
  } else {
    beep(2);
    notifier.notify({
      'title': 'Gulp Error',
      'subtitle': 'You must provide a flag to Gulp',
      'message': '`gulp --proto` or `gulp --dev`'
    });
    gutil.log(gutil.colors.bgRed.bold.white('========================================'));
    gutil.log(gutil.colors.bgRed.bold.white('ERROR: You must provide a flag to Gulp'));
    gutil.log(gutil.colors.bgRed.bold.white('========================================'));
    gutil.log(gutil.colors.bold.green('gulp --proto'), gutil.colors.white('for prototyping'));
    gutil.log(gutil.colors.bold.green('gulp --dev'), gutil.colors.white('for application/website work'));
    gutil.log('---');
    cb();
  }
});

// Development is when we're working on the actual
// Django website/application
gulp.task('development', function(cb) {
  // We use this variable to know what's going on,
  // particularly used in the webpack portion
  process.env.NODE_ENV = 'development';

  // gulp-sequence allows us to run tasks in a specific
  // order (normally Gulp uses "streams" which means tasks
  // run independent of each other, which is good but not
  // always what we want, ie. you want JS to be linted
  // before you webpack/uglify it)
  sequence('sprites', ['images', 'svgs', 'svg2jade'], 'sass', 'eslint','webpack', ['watch', 'browserSync'], cb);
});


// Prototype is when we're working through initial
// templates, aesthetics, and design decisions
gulp.task('prototype', function(cb) {
  process.env.NODE_ENV = 'prototype';
  sequence('clean', 'sprites', ['images',  'svgs', 'svg2jade'], 'jade', 'sass', 'eslint','webpack', ['watch', 'browserSync'], cb);
});


gulp.task('production', function(cb) {
  process.env.NODE_ENV = 'production';
  sequence('karma', ['images', 'svgs', 'svg2jade'], 'jade', 'sass', ['eslint', 'webpack'], cb);
});
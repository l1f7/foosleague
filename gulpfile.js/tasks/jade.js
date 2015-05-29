/**
 * Jade
 * ----------------------------------------------------
 * Super terse html preprocessor awesomeness
 */

var bs              = require('browser-sync')
,   config          = require('../config/jade')
,   gulp            = require('gulp')
,   jade            = require('gulp-jade')
,   print           = require('gulp-print')
,   jadeInheritance = require('gulp-jade-inheritance')
,   changed         = require('gulp-changed')
,   cached          = require('gulp-cached')
,   gulpif          = require('gulp-if')
,   filter          = require('gulp-filter')
,   handleErrors    = require('../lib/handleErrors');

function checkForPartials(file) {
  var pathChunks = file.relative.split('/');
  for (var i = pathChunks.length - 1; i >= 0; i--) {
    if (pathChunks[i].charAt(0) === '_'){
      return
    }
  };
  return file
}

gulp.task('jade', function() {
  if (global.jadeFirstCompile === undefined){
    return gulp.src(config.src)
      //filter out partials (folders and files starting with "_" )
      .pipe(filter(checkForPartials))
      .pipe(jade({ pretty: true }))
      .on('error', handleErrors)
      .pipe(gulp.dest(config.dest))
      .pipe(bs.reload({stream:true}));

  } else {
    return gulp.src(config.src)

      //only pass unchanged *main* files and *all* the partials
      .pipe(changed(config.dest, {extension: '.html'}))

      //filter out unchanged partials, but it only works when watching
      .pipe(cached('jade'))

      //find files that depend on the files that have changed
      .pipe(jadeInheritance({basedir: config.srcDir}))

      //filter out partials (folders and files starting with "_" )
      .pipe(filter(checkForPartials))

      //process jade templates
      .pipe(jade({ pretty: true }))

      .on('error', handleErrors)
      .pipe(gulp.dest(config.dest))
      .pipe(bs.reload({stream:true}));
  }
});
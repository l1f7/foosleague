/**
 * SVG Tasks
 * ----------------------------------------------------
 * Three things are happening in here:
 *    1. Minifying/cleanup of SVG images
 *    2. #1 + conversion to Jade templates for svg files
 *       that are to be inlined in the HTML
 *    3. #1 + conversion to svg sprite sheets
 */

var bs           = require('browser-sync')
,   changed      = require('gulp-changed')
,   config       = require('../config/svgs')
,   gulp         = require('gulp')
,   svgmin       = require('gulp-svgmin')
,   html2jade    = require('gulp-html2jade')
,   flatten      = require('gulp-flatten')
,   handleErrors = require('../lib/handleErrors')
,   svgSprite    = require('gulp-svg-sprite');


// Minify our normal SVG images
gulp.task('svgs', function() {
  gulp.src(config.svg.src)
    .pipe(changed(config.svg.dest)) // Ignore unchanged files
    .pipe(svgmin()) // Optimize
      .on('error', handleErrors)
    .pipe(gulp.dest(config.svg.dest))
    .pipe(bs.reload({stream:true}));

  return gulp.src(config.svg.spriteSrc)
});


// Minify our SVG images and convert
// into Jade templates
gulp.task('svg2jade', function () {
  return gulp.src(config.svg2jade.src)
    .pipe(changed(config.svg2jade.dest))
    .pipe(svgmin())
      .on('error', handleErrors)
    .pipe(html2jade(config.svg2jade.options))
      .on('error', handleErrors)
    .pipe(gulp.dest(config.svg2jade.dest))
    .pipe(bs.reload({stream:true}));
});


// Minify our SVGs and convert
// into SVG sprite sheets
gulp.task('sprites', function() {

  // Render a single sprite sheet
  function renderSprite(config) {
    return gulp.src(config.files)
      .pipe(svgmin()) // Optimize
      .pipe(svgSprite(config.config))
      .on('error', handleErrors)
      .pipe(gulp.dest(config.dest));
  }

  // Gulp SVG Sprite only renders a single svg
  // sprite per config (but it can output different
  // types of sprites from the same set of files), so
  // we are just looping through the number of dirs
  // in /raw/assets/sprites and then running a new
  // gulp-svg-sprite instance for each
  for (var i = config.sprites.configs.length - 1; i >= 0; i--) {
    renderSprite(config.sprites.configs[i]);
  };

  // Move our compiled sprite sheets into the
  // appropriate directory. Flatten just removes
  // the extra folders in the path structure:
  // - without flatten(): /prototype/assets/svgs/icons/symbol/icons.svg
  // - with flatten(): /prototype/assets/svgs/icons.svg
  return gulp.src(config.sprites.spriteFiles)
    .pipe(flatten())
    .pipe(gulp.dest(config.sprites.dest))
    .pipe(bs.reload({stream:true}));
});
var gulp    = require('gulp')
,   images  = require('../config/images')
,   svgs    = require('../config/svgs')
,   sass    = require('../config/sass')
,   jade    = require('../config/jade')
,   argv    = require('yargs').argv
,   webpack = require('../config/webpack')(process.env.NODE_ENV)
,   watch   = require('gulp-watch');

//gulp.task('watch', ['browserSync'], function() {
gulp.task('watch', function() {
  global.jadeFirstCompile = true

  watch(images.src,        function() { gulp.start('images'); });
  watch(svgs.svg.src,      function() { gulp.start('svgs'); });
  watch(svgs.svg2jade.src, function() { gulp.start('svg2jade'); });
  watch(svgs.sprites.all,  function() { gulp.start('sprites'); });
  watch(sass.src,          function() { gulp.start('cssmin'); });
  if (argv.proto) {
    watch(jade.src,        function() { gulp.start('jade'); });
  }
  watch(webpack.src,       function() { gulp.start('eslint', 'webpack'); });
});

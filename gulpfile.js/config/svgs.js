var config = require('./')
,   fs     = require('fs')
,   path   = require('path')
,   argv   = require('yargs').argv;

/**
 * svgmin config object
 */
module.exports.svg = {
  src: config.sourceAssets + 'svgs/**/!(sprite)*.svg',
  spriteSrc: config.sourceAssets + 'svgs/**/(sprite)*.svg',
  dest: (argv.proto) ? config.prototypeAssets + 'svgs' : config.appAssets + 'svgs'
}

/**
 * svg2jade config object
 */
module.exports.svg2jade = {
  src: config.sourceAssets + 'jade_svgs/*.svg',
  dest: config.sourceDirectory + 'templates/_svgs/',
  options: {
    nspaces: 2,
    donotencode: true,
    bodyless: true
  }
}


/**
 * --------------------------------------------------------------------------
 * svg sprites config object + helper functions
 * --------------------------------------------------------------------------
 */

// Get list of directory names
// @props: http://stackoverflow.com/a/24594123/1870528
function getDirectories (srcpath) {
  return fs.readdirSync(srcpath).filter(function(file) {
    var obj = fs.statSync(path.join(srcpath, file));
    if (obj.isDirectory()){
      return obj;
    }
  });
}

// Generate the config files for each set of sprites
// that we want to use (ie. one per folder)
function generateSpriteConfigs(srcpath) {
  var dirs = getDirectories(srcpath)
  ,   cfgs = [];

  for (var i = dirs.length - 1; i >= 0; i--) {
    // Kind of ugly, but using the config.sourceAssets path
    // (./src/assets) wasn't working because we aren't inside
    // of the Gulp/Node instance here, so require() was pathing
    // from this file @ `./gulpfile.js/config/svgs.js`
    var config = require('../../raw/assets/sprites/' + dirs[i] + '/config');

    // We also need to include the files and directory
    // that we want to be using with this config
    cfgs.push({
      config: config,
      files: srcpath + dirs[i] + '/*.svg',
      dest: srcpath + dirs[i]
    });
  };

  return cfgs;
}

/**
 * 1. Our sprites are created in folders nested inside of each directory,
 *    so our minimatch globs need to be very particular.
 *
 *    * = single level
 *    ** = infinite levels
 *
 *    For example, if the following folder:
 *    /raw/assets/sprites/icons
 *
 *    had several svg files in it that we then transform into a "css"
 *    sprite, then our final sprite is then created at:
 *    /raw/assets/sprites/icons/css/icons.svg
 *
 *    Hence, our watch task (all) will create an infinite loop if we're
 *    watching the svg sprite files, which is why we are only using the
 *    single star minimatch globs.
 */
module.exports.sprites = {
  all: config.sourceAssets + 'sprites/*/*.svg', /* 1 */
  configs: generateSpriteConfigs(config.sourceAssets + 'sprites/'),
  spriteFiles: config.sourceAssets + 'sprites/*/*/*.svg', /* 1 */
  dest: (argv.proto) ? config.prototypeAssets + 'svgs' : config.appAssets + 'svgs'
}
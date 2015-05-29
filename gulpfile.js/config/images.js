var config = require('./')
,   argv   = require('yargs').argv;

module.exports = {
  src: config.sourceAssets + "images/**",
  dest: (argv.proto) ? config.prototypeAssets + 'images' : config.appAssets + 'images'
}

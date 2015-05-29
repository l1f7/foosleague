var config = require('./')
,   argv   = require('yargs').argv;

module.exports = {
  srcDir: config.sourceDirectory + 'templates',
  src: config.sourceDirectory + 'templates/**/*.jade',
  dest: (argv.proto) ?
    config.prototypeDirectory :
    config.appDirectory + 'templates'
}
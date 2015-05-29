
var config = require('./')
,   argv   = require('yargs').argv;

if (argv.proto){
  module.exports = {
    port: 1337,
    server: {
      baseDir: config.prototypeDirectory
    },
    files: [config.prototypeDirectory +'**']
  }
} else {
  module.exports = {
    files: [
      config.appDirectory  + "static/**",
      config.appDirectory  + "templates/**/*.html"
    ],
    proxy: "localhost:8000",
    port: 1337,
    ghostMode: {
      clicks: true,
      forms: true,
      scroll: false
    }
  }
}
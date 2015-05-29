/**
 * This is our basic configuration object that gets exported
 * to be used by our other config files.
 *
 * var config = require('./');
 *
 * You'll see the above line at the top of each our config
 * files, all that's doing is requiring this file.
 */

var config = {}

// source
config.sourceDirectory    = './raw/';
config.sourceAssets       = config.sourceDirectory + 'assets/';

// prototype directory
config.prototypeDirectory = './prototype/';
config.prototypeAssets    = config.prototypeDirectory + 'assets/';

// build directory
config.appDirectory       = './website/foosleague/';
config.appAssets          = config.appDirectory + 'static/';

module.exports = config;
var config        = require('./')
,   karmaWebpack  = require('karma-webpack')
,   webpackConfig = require('./webpack')('test')

module.exports = {
  frameworks: ['mocha', 'sinon-chai'],
  files: [
    './src/js/**/__tests__/*'
  ],
  preprocessors: {
    './src/js/**/__tests__/*': ['webpack']
  },
  webpack: webpackConfig,
  singleRun: process.env.TRAVIS_CI === 'true',
  reporters: ['nyan'],
  browsers: [(process.env.TRAVIS_CI === 'true'? 'Firefox' : 'Chrome')]
}

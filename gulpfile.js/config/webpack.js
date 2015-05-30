var config          = require('./')
,   webpack         = require('webpack')
,   webpackManifest = require('../lib/webpackManifest')
,   argv            = require('yargs').argv;

module.exports = function(env) {
  var jsDest
  ,   jsSrc  = config.sourceDirectory + 'js/';

  jsDest = (argv.proto) ? config.prototypeAssets + 'js/' : config.appAssets + 'js/'

  var webpackConfig = {
    // Entry will be the files created by Webpack
    // (in this case there would be two files)
    src : jsSrc + '**',
    entry: {
      app:  [jsSrc + 'App.js']
    },

    output: {
      path: jsDest,
      //filename: '[name].js',
      // from greypants' gulp starter, not sure the use yet
      filename: env === 'production' ? '[name]-[hash].js' : '[name].js',
      publicPath: '/assets/js/'
    },

    plugins: [],

    resolve: {
      extensions: ['', '.js', '.jsx', '.coffee']
    },

    module: {
      loaders: [
        {
          test: /\.js$/,
          loader: 'babel-loader?stage=1',
          exclude: /node_modules/
        }
      ]
    }
  }

  // if (env !== 'test') {
  //   // Factor out common dependencies into a common.js
  //   webpackConfig.plugins.push(
  //     new webpack.optimize.CommonsChunkPlugin({
  //       name: 'common',
  //       filename: env === 'production' ? '[name]-[hash].js' : '[name].js',
  //     })
  //   )
  // }

  if (env === 'development' || env === 'prototype') {
    webpackConfig.devtool = 'source-map'
    webpack.debug = true
  }

  if (env === 'production') {
    webpackConfig.plugins.push(
      new webpackManifest(publicPath, 'public'),
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('production')
        }
      }),
      new webpack.optimize.DedupePlugin(),
      new webpack.optimize.UglifyJsPlugin(),
      new webpack.NoErrorsPlugin()
    )
  }

  return webpackConfig
}
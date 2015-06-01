(function (window, $) {
  'use strict';

  var LIFT, UTIL;

  LIFT = {

    // common gets called for every single page/view which means
    // global elements should be contained in here
    // ie. global navigation
    common: {

      init: function () {
        console.log('APP INTIALIZED');
      },
    },


    home: {
      init: function () {
        require.ensure([], function () {
          var Feed = require('./feed.js');
          Feed.init();
        });
      }
    }
  };

  UTIL = {
    exec: function (model, action) {
      var ns = LIFT;

      action = (action === undefined) ? 'init' : action;

      if (model !== '' && ns[model] && typeof ns[model][action] === 'function') {
        ns[model][action]();
      }
    },

    init: function () {
      // the following looks for an element with a class "mainblock"
      // and then pulls the value of it's data-model attribute
      // ie.: <div class="mainblock" data-model="myModel">
      var initializer = document.getElementsByClassName('l-site');
      var model       = initializer[0].getAttribute('data-model');

      UTIL.exec('common'); // calls LIFT.common.init()
      UTIL.exec(model);    // calls LIFT.model.init()
    }
  };

  // DOM ready, let's DO DIS!
  $(document).ready(UTIL.init);

})(window, jQuery);
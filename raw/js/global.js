module.exports = {
  // clickHandler is used for any jquery.on events, so that we
  // can properly handle mobile/touch events
  clickHandler: ('ontouchstart' in document.documentElement ? 'touchstart' : 'click'),
  windowWidth: $(window).width(),
  windowHeight: $(window).height(),

  // utility in case we need to listen for events that propagate
  // all the way up to the body/sitewrap tag
  siteWrapper: $('.l-site'),

  /** getCSRF
   *  CROSS SITE REQUEST FORGERY
   *  Only needed if you're doing AJAX
   *  @ref: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax
   */
  getCSRF: function (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  },

  csrfSafeMethod: function (method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
}
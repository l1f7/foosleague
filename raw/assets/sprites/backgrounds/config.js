/**
 * 1. You can configure multiple mode outputs if you would like to, see:
 *    https://github.com/jkphl/svg-sprite/blob/master/docs/configuration.md#output-modes
 *
 * 2. Pathing inside of the svg-sprite library is _super_ confusing. See this link:
 *    https://github.com/jkphl/svg-sprite#output-destinations
 *    Ultimately, it's standard format is to build out files/folders nested
 *    inside of the destination directory (./raw/assets/svgs)... but that isn't
 *    where we want most things so that's why the paths are so ridiculous.
 *
 * 3. Removes the normal prefix in our SASS/CSS files, ie:
 *      - .svg-accessbility {}  --> this is the normal sass output
 *      - .accessibility {}     --> this is the new sass output
 */

module.exports = {
  mode : { /* 1 */
    view : {
      sprite: 'backgrounds-view', /* 2 */
      prefix: '.%s', /* 3 */
      bust : false,
      example: true,
      render : {
        scss: true
        // scss : {
        //   dest: '../../../../sass/sprites/_backgrounds-view' /* 2 */
        // }
      }
    },
  }
}
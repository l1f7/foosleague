var gulp         = require('gulp')
,   config       = require('../config/eslint')
,   eslint       = require('gulp-eslint')
,   beep         = require('beepbeep')
,   notifier     = require('gulp-notify/node_modules/node-notifier')
,   gutil        = require('gulp-util')
,   handleErrors = require('../lib/handleErrors')
,   table        = require("text-table")
,   scope        = this;


gulp.task('eslint', function () {
  return gulp.src(config.src)
    .pipe(eslint(config.eslintcfg))
    .on('error', handleErrors)
    .pipe(eslint.format(function (results) {
      var formattedResults = formatter(results);
      if (formattedResults !== ''){
        beep(2);
        notifier.notify({
          'title': 'ESLint',
          'message': 'Found ' + formattedResults[1] + ' problems'
        });
        gutil.log(gutil.colors.bgRed.bold.white('========================================'));
        gutil.log(gutil.colors.bgRed.bold.white('ESLint Problems                         '));
        gutil.log(gutil.colors.bgRed.bold.white('========================================'));
        gutil.log(formattedResults[2]);
        console.log(formattedResults[0]);
      }
    }));
});

//------------------------------------------------------------------------------
// Helpers
//------------------------------------------------------------------------------

/**
 * Given a word and a count, append an s if count is not one.
 * @param {string} word A word in its singular form.
 * @param {int} count A number controlling whether word should be pluralized.
 * @returns {string} The original word with an s on the end if count is not one.
 */
function pluralize(word, count) {
    return (count === 1 ? word : word + "s");
}

//------------------------------------------------------------------------------
// Public Interface
//------------------------------------------------------------------------------

function formatter(results) {

  var output = "\n"
  ,   total = 0
  ,   errors = 0
  ,   warnings = 0
  ,   summaryColor = "yellow"
  ,   totalOutput = "";

  results.forEach(function(result) {
    var messages = result.messages;

    if (messages.length === 0) {
      return;
    }

    total += messages.length;
    output += gutil.colors.underline(result.filePath) + "\n";

    output += table(
      messages.map(function(message) {
        var messageType;

        if (message.fatal || message.severity === 2) {
          messageType = gutil.colors.red("error");
          summaryColor = "red";
          errors++;
        } else {
          messageType = gutil.colors.yellow("warning");
          warnings++;
        }

        return [
          "",
          message.line || 0,
          message.column || 0,
          messageType,
          message.message.replace(/\.$/, ""),
          gutil.colors.gray(message.ruleId || "")
        ];
      }),
      {
        align: ["", "r", "l"],
        stringLength: function(str) {
          return gutil.colors.stripColor(str).length;
        }
      }
    ).split("\n").map(function(el) {
      return el.replace(/(\d+)\s+(\d+)/, function(m, p1, p2) {
        return gutil.colors.gray(p1 + ":" + p2);
      });
    }).join("\n") + "\n\n";
  });

  if (total > 0) {
    totalOutput += gutil.colors[summaryColor].bold([
      "\u2716 ", total, pluralize(" problem", total),
      " (", errors, pluralize(" error", errors), ", ",
      warnings, pluralize(" warning", warnings), ")"
    ].join(""));
  }

  return total > 0 ? [output, total, totalOutput] : "";
};
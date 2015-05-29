var config = require('./')

// @props: https://raw.githubusercontent.com/airbnb/javascript/master/linters/.eslintrc
module.exports = {
  src: config.sourceDirectory + 'js/**/*.js',
  'parser': 'babel-eslint',
  'globals': {
    'jQuery':false,
    '$':true
  },

  'env': {
    'browser': true,
    'jquery': true,
    'node': true
  },

  'rules': {
  /**
   * Strict mode
   */

    'strict': [2, 'never'],           // babel inserts 'use strict'; for us
                                      // http://eslint.org/docs/rules/strict

  /**
   * Variables
   */
    'no-shadow': 2,                  // disallow declaration of variables already declared in the outer scope
                                     // http://eslint.org/docs/rules/no-shadow

    'no-shadow-restricted-names': 2, // disallow shadowing of names such as arguments
                                     // http://eslint.org/docs/rules/no-shadow-restricted-names

    'no-unused-vars': [2, {          // disallow declaration of variables that are not used in the code
      'vars': 'local',               // http://eslint.org/docs/rules/no-unused-vars
      'args': 'after-used'
    }],

    'no-use-before-define': 2,       // disallow use of variables before they are defined
                                     // http://eslint.org/docs/rules/no-use-before-define

  /**
   * Possible errors
   */
    'comma-dangle': [2, 'never'],    // disallow or enforce trailing commas
                                     // http://eslint.org/docs/rules/comma-dangle

    'no-cond-assign': [2, 'always'], // disallow assignment in conditional expressions
                                     // http://eslint.org/docs/rules/no-cond-assign

    'no-console': 1,                 // disallow use of console (off by default in the node environment)
                                     // http://eslint.org/docs/rules/no-console

    'no-debugger': 1,                // disallow use of debugger
                                     // http://eslint.org/docs/rules/no-debugger

    'no-alert': 1,                   // http://eslint.org/docs/rules/no-alert

    'no-constant-condition': 1,      // disallow use of constant expressions in conditions
                                     // http://eslint.org/docs/rules/no-constant-condition

    'no-dupe-keys': 2,               // disallow duplicate keys when creating object literals
                                     // http://eslint.org/docs/rules/no-dupe-keys

    'no-duplicate-case': 2,          // disallow a duplicate case label.
                                     // http://eslint.org/docs/rules/no-duplicate-case

    'no-empty': 2,                   // disallow empty statements
                                     // http://eslint.org/docs/rules/no-empty

    'no-ex-assign': 2,               // disallow assigning to the exception in a catch block
                                     // http://eslint.org/docs/rules/no-ex-assign

    'no-extra-boolean-cast': 0,      // disallow double-negation boolean casts in a boolean context
                                     // http://eslint.org/docs/rules/no-extra-boolean-cast

    'no-extra-semi': 2,              // disallow unnecessary semicolons
                                     // http://eslint.org/docs/rules/no-extra-semi

    'no-func-assign': 2,             // disallow overwriting functions written as function declarations
                                     // http://eslint.org/docs/rules/no-func-assign

    'no-inner-declarations': 2,      // disallow function or variable declarations in nested blocks
                                     // http://eslint.org/docs/rules/no-inner-declarations

    'no-invalid-regexp': 2,          // disallow invalid regular expression strings in the RegExp constructor
                                     // http://eslint.org/docs/rules/no-invalid-regexp

    'no-irregular-whitespace': 2,    // disallow irregular whitespace outside of strings and comments
                                     // http://eslint.org/docs/rules/no-irregular-whitespace

    'no-obj-calls': 2,               // disallow the use of object properties of the global object (Math and JSON) as functions
                                     // http://eslint.org/docs/rules/no-obj-calls

    'no-reserved-keys': 2,           // disallow reserved words being used as object literal keys (off by default)
                                     // http://eslint.org/docs/rules/no-reserved-keys

    'no-sparse-arrays': 2,           // disallow sparse arrays
                                     // http://eslint.org/docs/rules/no-sparse-arrays

    'no-unreachable': 2,             // disallow unreachable statements after a return, throw, continue, or break statement
                                     // http://eslint.org/docs/rules/no-unreachable

    'use-isnan': 2,                  // disallow comparisons with the value NaN
                                     // http://eslint.org/docs/rules/use-isnan

  /**
   * Best practices
   */

    'block-scoped-var': 2,           // treat var statements as if they were block scoped (off by default).
                                     // http://eslint.org/docs/rules/block-scoped-var

    'consistent-return': 2,          // require return statements to either always or never specify values
                                     // http://eslint.org/docs/rules/consistent-return

    'curly': [2, 'multi-line'],      // specify curly brace conventions for all control statements
                                     // http://eslint.org/docs/rules/curly

    'default-case': 2,               // require default case in switch statements (off by default)
                                     // http://eslint.org/docs/rules/default-case

    'dot-notation': [2, {            // encourages use of dot notation whenever possible
      'allowKeywords': true          // http://eslint.org/docs/rules/dot-notation
    }],

    'eqeqeq': 2,                     // require the use of === and !==
                                     // http://eslint.org/docs/rules/eqeqeq

    'guard-for-in': 2,               // make sure for-in loops have an if statement (off by default)
                                     // http://eslint.org/docs/rules/guard-for-in

    'no-caller': 2,                  // disallow use of arguments.caller or arguments.callee
                                     // http://eslint.org/docs/rules/no-caller

    'no-else-return': 2,             // disallow else after a return in an if (off by default)
                                     // http://eslint.org/docs/rules/no-else-return

    'no-eq-null': 2,                 // disallow comparisons to null without a type-checking operator (off by default)
                                     // http://eslint.org/docs/rules/no-eq-null

    'no-eval': 2,                    // disallow use of eval()
                                     // http://eslint.org/docs/rules/no-eval

    'no-extend-native': 2,           // disallow adding to native types
                                     // http://eslint.org/docs/rules/no-extend-native

    'no-extra-bind': 2,              // disallow unnecessary function binding
                                     // http://eslint.org/docs/rules/no-extra-bind

    'no-fallthrough': 2,             // disallow fallthrough of case statements
                                     // http://eslint.org/docs/rules/no-fallthrough

    'no-floating-decimal': 2,        // disallow the use of leading or trailing decimal points in numeric literals (off by default)
                                     // http://eslint.org/docs/rules/no-floating-decimal

    'no-implied-eval': 2,            // disallow use of eval()-like methods
                                     // http://eslint.org/docs/rules/no-implied-eval

    'no-lone-blocks': 2,             // disallow unnecessary nested blocks
                                     // http://eslint.org/docs/rules/no-lone-blocks

    'no-loop-func': 2,               // disallow creation of functions within loops
                                     // http://eslint.org/docs/rules/no-loop-func

    'no-multi-str': 2,               // disallow use of multiline strings
                                     // http://eslint.org/docs/rules/no-multi-str

    'no-native-reassign': 2,         // disallow reassignments of native objects
                                     // http://eslint.org/docs/rules/no-native-reassign

    'no-new': 2,                     // disallow use of new operator when not part of the assignment or comparison
                                     // http://eslint.org/docs/rules/no-new

    'no-new-func': 2,                // disallow use of new operator for Function object
                                     // http://eslint.org/docs/rules/no-new-func

    'no-new-wrappers': 2,            // disallows creating new instances of String,Number, and Boolean
                                     // http://eslint.org/docs/rules/no-new-wrappers

    'no-octal': 2,                   // disallow use of octal literals
                                     // http://eslint.org/docs/rules/no-octal

    'no-octal-escape': 2,            // disallow use of octal escape sequences in string literals, such as var foo = "Copyright \251";
                                     // http://eslint.org/docs/rules/no-octal-escape

    'no-param-reassign': 2,          // disallow reassignment of function parameters (off by default)
                                     // http://eslint.org/docs/rules/no-param-reassign

    'no-proto': 2,                   // disallow usage of __proto__ property
                                     // http://eslint.org/docs/rules/no-proto

    'no-redeclare': 2,               // disallow declaring the same variable more then once
                                     // http://eslint.org/docs/rules/no-redeclare

    'no-return-assign': 2,           // disallow use of assignment in return statement
                                     // http://eslint.org/docs/rules/no-return-assign

    'no-script-url': 2,              // disallow use of javascript: urls.
                                     // http://eslint.org/docs/rules/no-script-url

    'no-self-compare': 2,            // disallow comparisons where both sides are exactly the same (off by default)
                                     // http://eslint.org/docs/rules/no-self-compare

    'no-sequences': 2,               // disallow use of comma operator
                                     // http://eslint.org/docs/rules/no-sequences

    'no-throw-literal': 2,           // restrict what can be thrown as an exception (off by default)
                                     // http://eslint.org/docs/rules/no-throw-literal

    'no-with': 2,                    // disallow use of the with statement
                                     // http://eslint.org/docs/rules/no-with

    'radix': 2,                      // require use of the second argument for parseInt() (off by default)
                                     // http://eslint.org/docs/rules/radix

    'vars-on-top': 2,                // requires to declare all vars on top of their containing scope (off by default)
                                     // http://eslint.org/docs/rules/vars-on-top

    'wrap-iife': [2, 'any'],         // require immediate function invocation to be wrapped in parentheses (off by default)
                                     // http://eslint.org/docs/rules/wrap-iife

    'yoda': 2,                       // require or disallow Yoda conditions
                                     // http://eslint.org/docs/rules/yoda

  /**
   * Style
   */
    'indent': [2, 2],                // this option sets a specific tab width for your code (off by default)
                                     // http://eslint.org/docs/rules/

    'brace-style': [2,               // enforce one true brace style (off by default)
      '1tbs', {                      // http://eslint.org/docs/rules/brace-style
      'allowSingleLine': true
    }],

    'quotes': [                      // specify whether double or single quotes should be used
      2, 'single', 'avoid-escape'    // http://eslint.org/docs/rules/quotes

    ],

    'camelcase': [2, {               // require camel case names
      'properties': 'never'          // http://eslint.org/docs/rules/camelcase
    }],

    'comma-spacing': [2, {           // enforce spacing before and after comma
      'before': false,               // http://eslint.org/docs/rules/comma-spacing
      'after': true
    }],

    'comma-style': [2, 'last'],      // enforce one true comma style (off by default)
                                     // http://eslint.org/docs/rules/comma-style

    'eol-last': 2,                   // enforce newline at the end of file, with no multiple empty lines
                                     // http://eslint.org/docs/rules/eol-last

    'func-names': 1,                 // require function expressions to have a name (off by default)
                                     // http://eslint.org/docs/rules/func-names

    'key-spacing': [2, {             // enforces spacing between keys and values in object literal properties
        'beforeColon': false,        // http://eslint.org/docs/rules/key-spacing
        'afterColon': true
    }],

    'new-cap': [2, {                 // require a capital letter for constructors
      'newIsCap': true               // http://eslint.org/docs/rules/new-cap
    }],

    'no-multiple-empty-lines': [2, { // disallow multiple empty lines (off by default)
      'max': 2                       // http://eslint.org/docs/rules/no-multiple-empty-lines
    }],

    'no-nested-ternary': 2,          // disallow nested ternary expressions (off by default)
                                     // http://eslint.org/docs/rules/no-nested-ternary

    'no-new-object': 2,              // disallow use of the Object constructor
                                     // http://eslint.org/docs/rules/no-new-object

    'no-spaced-func': 2,             // disallow space between function identifier and application
                                     // http://eslint.org/docs/rules/no-spaced-func

    'no-trailing-spaces': 2,         // disallow trailing whitespace at the end of lines
                                     // http://eslint.org/docs/rules/no-trailing-spaces

    'no-wrap-func': 2,               // disallow wrapping of non-IIFE statements in parens
                                     // http://eslint.org/docs/rules/no-wrap-func

    'no-underscore-dangle': 0,       // disallow dangling underscores in identifiers
                                     // http://eslint.org/docs/rules/no-underscore-dangle

    'one-var': [2, 'never'],         // allow just one var statement per function (off by default)
                                     // http://eslint.org/docs/rules/one-var

    'padded-blocks': [2, 'never'],   // enforce padding within blocks (off by default)
                                     // http://eslint.org/docs/rules/padded-blocks

    'semi': [2, 'always'],           // require or disallow use of semicolons instead of ASI
                                     // http://eslint.org/docs/rules/semi

    'semi-spacing': [2, {            // enforce spacing before and after semicolons
      'before': false,               // http://eslint.org/docs/rules/semi-spacing
      'after': true
    }],

    'space-after-keywords': 2,       // require a space after certain keywords (off by default)
                                     // http://eslint.org/docs/rules/space-after-keywords

    'space-before-blocks': 2,        // require or disallow space before blocks (off by default)
                                     // http://eslint.org/docs/rules/space-before-blocks

    'space-before-function-paren': [2, 'never'], // require or disallow space before function opening parenthesis (off by default)
                                     // http://eslint.org/docs/rules/space-before-function-paren

    'space-infix-ops': 2,            // require spaces around operators
                                     // http://eslint.org/docs/rules/space-infix-ops

    'space-return-throw-case': 2,    // require a space after return, throw, and case
                                     // http://eslint.org/docs/rules/space-return-throw-case

    'spaced-line-comment': 2,        // require or disallow a space immediately following the // in a line comment (off by default)
                                     // http://eslint.org/docs/rules/spaced-line-comment
  }
}



// // @props: https://raw.githubusercontent.com/airbnb/javascript/master/linters/.eslintrc
// module.exports = {
//   src: config.sourceDirectory + 'js/**/*.js',
//   eslintcfg: {

//     'parser': 'babel-eslint',
//     'globals': {
//       'jQuery':false,
//       '$':true
//     },
//     'envs': {
//       'browser': true,
//       'jquery': true,
//       'jasmine': true,
//       'node': true
//     },
//     'ecmaFeatures': {
//       'arrowFunctions': true,
//       'binaryLiterals': true,
//       'blockBindings': true,
//       'classes': true,
//       'defaultParams': true,
//       'destructuring': true,
//       'forOf': true,
//       'generators': false,
//       'modules': true,
//       'objectLiteralComputedProperties': true,
//       'objectLiteralDuplicateProperties': false,
//       'objectLiteralShorthandMethods': true,
//       'objectLiteralShorthandProperties': true,
//       'spread': true,
//       'superInFunctions': true,
//       'templateStrings': true,
//       'jsx': true,
//       'unicodeCodePointEscapes': false,
//       'globalReturn': false,
//       'octalLiterals': false,
//       'regexUFlag': false,
//       'regexYFlag': false,
//     },
//     'rules': {
// /**
//  * Strict mode
//  */
//     // babel inserts 'use strict'; for us
//     // http://eslint.org/docs/rules/strict
//     'strict': [2, 'never'],

// /**
//  * ES6
//  */
//     'no-var': 2,                     // http://eslint.org/docs/rules/no-var

// /**
//  * Variables
//  */
//     'no-shadow': 2,                  // http://eslint.org/docs/rules/no-shadow
//     'no-shadow-restricted-names': 2, // http://eslint.org/docs/rules/no-shadow-restricted-names
//     'no-unused-vars': [2, {          // http://eslint.org/docs/rules/no-unused-vars
//       'vars': 'local',
//       'args': 'after-used'
//     }],
//     'no-use-before-define': 2,       // http://eslint.org/docs/rules/no-use-before-define

// /**
//  * Possible errors
//  */
//     'comma-dangle': [2, 'never'],    // http://eslint.org/docs/rules/comma-dangle
//     'no-cond-assign': [2, 'always'], // http://eslint.org/docs/rules/no-cond-assign
//     'no-console': 1,                 // http://eslint.org/docs/rules/no-console
//     'no-debugger': 1,                // http://eslint.org/docs/rules/no-debugger
//     'no-alert': 1,                   // http://eslint.org/docs/rules/no-alert
//     'no-constant-condition': 1,      // http://eslint.org/docs/rules/no-constant-condition
//     'no-dupe-keys': 2,               // http://eslint.org/docs/rules/no-dupe-keys
//     'no-duplicate-case': 2,          // http://eslint.org/docs/rules/no-duplicate-case
//     'no-empty': 2,                   // http://eslint.org/docs/rules/no-empty
//     'no-ex-assign': 2,               // http://eslint.org/docs/rules/no-ex-assign
//     'no-extra-boolean-cast': 0,      // http://eslint.org/docs/rules/no-extra-boolean-cast
//     'no-extra-semi': 2,              // http://eslint.org/docs/rules/no-extra-semi
//     'no-func-assign': 2,             // http://eslint.org/docs/rules/no-func-assign
//     'no-inner-declarations': 2,      // http://eslint.org/docs/rules/no-inner-declarations
//     'no-invalid-regexp': 2,          // http://eslint.org/docs/rules/no-invalid-regexp
//     'no-irregular-whitespace': 2,    // http://eslint.org/docs/rules/no-irregular-whitespace
//     'no-obj-calls': 2,               // http://eslint.org/docs/rules/no-obj-calls
//     'no-reserved-keys': 2,           // http://eslint.org/docs/rules/no-reserved-keys
//     'no-sparse-arrays': 2,           // http://eslint.org/docs/rules/no-sparse-arrays
//     'no-unreachable': 2,             // http://eslint.org/docs/rules/no-unreachable
//     'use-isnan': 2,                  // http://eslint.org/docs/rules/use-isnan
//     'block-scoped-var': 2,           // http://eslint.org/docs/rules/block-scoped-var

// /**
//  * Best practices
//  */
//     'consistent-return': 2,          // http://eslint.org/docs/rules/consistent-return
//     'curly': [2, 'multi-line'],      // http://eslint.org/docs/rules/curly
//     'default-case': 2,               // http://eslint.org/docs/rules/default-case
//     'dot-notation': [2, {            // http://eslint.org/docs/rules/dot-notation
//       'allowKeywords': true
//     }],
//     'eqeqeq': 2,                     // http://eslint.org/docs/rules/eqeqeq
//     'guard-for-in': 2,               // http://eslint.org/docs/rules/guard-for-in
//     'no-caller': 2,                  // http://eslint.org/docs/rules/no-caller
//     'no-else-return': 2,             // http://eslint.org/docs/rules/no-else-return
//     'no-eq-null': 2,                 // http://eslint.org/docs/rules/no-eq-null
//     'no-eval': 2,                    // http://eslint.org/docs/rules/no-eval
//     'no-extend-native': 2,           // http://eslint.org/docs/rules/no-extend-native
//     'no-extra-bind': 2,              // http://eslint.org/docs/rules/no-extra-bind
//     'no-fallthrough': 2,             // http://eslint.org/docs/rules/no-fallthrough
//     'no-floating-decimal': 2,        // http://eslint.org/docs/rules/no-floating-decimal
//     'no-implied-eval': 2,            // http://eslint.org/docs/rules/no-implied-eval
//     'no-lone-blocks': 2,             // http://eslint.org/docs/rules/no-lone-blocks
//     'no-loop-func': 2,               // http://eslint.org/docs/rules/no-loop-func
//     'no-multi-str': 2,               // http://eslint.org/docs/rules/no-multi-str
//     'no-native-reassign': 2,         // http://eslint.org/docs/rules/no-native-reassign
//     'no-new': 2,                     // http://eslint.org/docs/rules/no-new
//     'no-new-func': 2,                // http://eslint.org/docs/rules/no-new-func
//     'no-new-wrappers': 2,            // http://eslint.org/docs/rules/no-new-wrappers
//     'no-octal': 2,                   // http://eslint.org/docs/rules/no-octal
//     'no-octal-escape': 2,            // http://eslint.org/docs/rules/no-octal-escape
//     'no-param-reassign': 2,          // http://eslint.org/docs/rules/no-param-reassign
//     'no-proto': 2,                   // http://eslint.org/docs/rules/no-proto
//     'no-redeclare': 2,               // http://eslint.org/docs/rules/no-redeclare
//     'no-return-assign': 2,           // http://eslint.org/docs/rules/no-return-assign
//     'no-script-url': 2,              // http://eslint.org/docs/rules/no-script-url
//     'no-self-compare': 2,            // http://eslint.org/docs/rules/no-self-compare
//     'no-sequences': 2,               // http://eslint.org/docs/rules/no-sequences
//     'no-throw-literal': 2,           // http://eslint.org/docs/rules/no-throw-literal
//     'no-with': 2,                    // http://eslint.org/docs/rules/no-with
//     'radix': 2,                      // http://eslint.org/docs/rules/radix
//     'vars-on-top': 2,                // http://eslint.org/docs/rules/vars-on-top
//     'wrap-iife': [2, 'any'],         // http://eslint.org/docs/rules/wrap-iife
//     'yoda': 2,                       // http://eslint.org/docs/rules/yoda

// /**
//  * Style
//  */
//     'indent': [2, 2],                // http://eslint.org/docs/rules/
//     'brace-style': [2,               // http://eslint.org/docs/rules/brace-style
//       '1tbs', {
//       'allowSingleLine': true
//     }],
//     'quotes': [
//       2, 'single', 'avoid-escape'    // http://eslint.org/docs/rules/quotes
//     ],
//     'camelcase': [2, {               // http://eslint.org/docs/rules/camelcase
//       'properties': 'never'
//     }],
//     'comma-spacing': [2, {           // http://eslint.org/docs/rules/comma-spacing
//       'before': false,
//       'after': true
//     }],
//     'comma-style': [2, 'last'],      // http://eslint.org/docs/rules/comma-style
//     'eol-last': 2,                   // http://eslint.org/docs/rules/eol-last
//     'func-names': 1,                 // http://eslint.org/docs/rules/func-names
//     'key-spacing': [2, {             // http://eslint.org/docs/rules/key-spacing
//         'beforeColon': false,
//         'afterColon': true
//     }],
//     'new-cap': [2, {                 // http://eslint.org/docs/rules/new-cap
//       'newIsCap': true
//     }],
//     'no-multiple-empty-lines': [2, { // http://eslint.org/docs/rules/no-multiple-empty-lines
//       'max': 2
//     }],
//     'no-nested-ternary': 2,          // http://eslint.org/docs/rules/no-nested-ternary
//     'no-new-object': 2,              // http://eslint.org/docs/rules/no-new-object
//     'no-spaced-func': 2,             // http://eslint.org/docs/rules/no-spaced-func
//     'no-trailing-spaces': 2,         // http://eslint.org/docs/rules/no-trailing-spaces
//     'no-wrap-func': 2,               // http://eslint.org/docs/rules/no-wrap-func
//     'no-underscore-dangle': 0,       // http://eslint.org/docs/rules/no-underscore-dangle
//     'one-var': [2, 'never'],         // http://eslint.org/docs/rules/one-var
//     'padded-blocks': [2, 'never'],   // http://eslint.org/docs/rules/padded-blocks
//     'semi': [2, 'always'],           // http://eslint.org/docs/rules/semi
//     'semi-spacing': [2, {            // http://eslint.org/docs/rules/semi-spacing
//       'before': false,
//       'after': true
//     }],
//     'space-after-keywords': 2,       // http://eslint.org/docs/rules/space-after-keywords
//     'space-before-blocks': 2,        // http://eslint.org/docs/rules/space-before-blocks
//     'space-before-function-paren': [2, 'never'], // http://eslint.org/docs/rules/space-before-function-paren
//     'space-infix-ops': 2,            // http://eslint.org/docs/rules/space-infix-ops
//     'space-return-throw-case': 2,    // http://eslint.org/docs/rules/space-return-throw-case
//     'spaced-line-comment': 2         // http://eslint.org/docs/rules/spaced-line-comment
//   }
//   }
// }
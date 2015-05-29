## Setting up the development environment

This is based off of the normal Lift Dev Environment document, so there shouldn't be any major surprises here. From the root directory run:
`npm install && bower install`

## Directory Structure

The `raw/` folder is where all frontend dev should happen. The working SCSS, JS, SVGs, images, and prototype templates are stored here as well as the Bower components.

## Build Processes

### `gulp`
Gulp is the `default` task and fires off the `development` task. It does the following, in this order:
  * Compress/minify Images and SVG files into the `./website/PROJECTNAME/static/images` and `./website/PROJECTNAME/static/svgs`
  * Generate svg-sprite sheets as well as the SASS (if applicable) for them into the `./raw/assets/svgs` directory (and `./raw/sass/sprites` directory for those sprites that require css)
  * Compile `SASS` into the `./website/PROJECTNAME/static/css` directory
  * Lint the javascript, and then run it through Webpack to generate your javascript files into the `./website/PROJECTNAME/static/js` directory
  * Runs a `browser-sync` instance accessed at `localhost:1337` which proxies the Django project through it and then will automatically refresh every time you add changes images, svgs, css, or javascript

### `gulp prototype`
Gulp `prototype` does essentially the same things as `gulp`/`gulp development`, but compiles your files into the `./prototype` directory and runs the `jade` task so that you can quickly iterate on project ideas/layouts/modules before the project moves into development.

### `gulp production`
Gulp `production` is specifically for doing builds before you push to production. It works mostly the same as the main `development` task but uses `karma` to run any javascript tests and also compresses/uglifies the javascript which the normal `gulp development` tasks doesn't.

## Customizing Gulp
The `gulpfile.js` directory contains all of the configuration/tasks for the various gulp tasks that are run. You generally shouldn't need to edit too much, but in case you do, it's all there and heavily documented so it should be pretty easy to dive into and understand what's going on.


'use strict';
const argv = require('optimist').argv;
const child = require('./child');

const exitCode = argv.code || 0;

console.log('Parent script is up!');

child.run(exitCode);

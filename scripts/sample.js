'use strict';

const argv = require('optimist').argv;
const exitCode = argv.code || 0;

console.log('This is sample.js with code:', exitCode);

setTimeout(function () {
    console.log('Script is done');
    process.exit(exitCode);
}, 200);

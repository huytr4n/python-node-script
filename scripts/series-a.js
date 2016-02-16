'use strict';

console.log('This is series A');

setTimeout(function () {
    console.log('Series A is done');

    process.exit(0);
}, 200);

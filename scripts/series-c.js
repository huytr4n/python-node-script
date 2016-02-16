'use strict';

console.log('This is series C');

setTimeout(function () {
    console.log('Series C is done');

    process.exit(0);
}, 200);

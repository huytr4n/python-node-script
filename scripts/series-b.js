'use strict';

console.log('This is series B');

setTimeout(function () {
    console.log('Series B is done');

    process.exit(0);
}, 200);

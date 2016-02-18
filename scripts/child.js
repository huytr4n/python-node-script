'use strict';

console.log('Child script is up!');

/**
 * Expose.
 */
module.exports = {
    run: function (code) {
        setTimeout(function () {
            console.log('Child script is done!');
            process.exit(code);
        }, 200);
    }
}

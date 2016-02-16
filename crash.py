from Naked.toolshed.shell import muterun_js

response = muterun_js('scripts/crash.js')

print 'Done script with result: %s' % response.exitcode

if response == 0:
    # this should not happend
    print 'We should continue the next script'
else:
    print 'The script exit with crash code, we should stop here'

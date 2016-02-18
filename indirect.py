from Naked.toolshed.shell import execute_js

# success case
success = execute_js('scripts/parent.js --code=0')
print '==============================================='
print 'Run script with exit code 0'
print 'Sample script is done with result: %s' % success
print '==============================================='

# failed case
failed = execute_js('scripts/parent.js --code=1')
print '==============================================='
print 'Run script with exit code 1'
print 'Sample script is done with result: %s' % failed
print '==============================================='

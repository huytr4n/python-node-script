from Naked.toolshed.shell import execute_js

# success case
success = execute_js('scripts/sample.js')
print 'Sample script is done with result: %s' % success

# failed case
failed = execute_js('scripts/sample.js --code=1')
print 'Sample script is done with result: %s' % failed

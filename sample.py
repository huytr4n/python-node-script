from Naked.toolshed.shell import execute_js

success = execute_js('scripts/sample.js')

print 'Sample script is done with result: %s' % success

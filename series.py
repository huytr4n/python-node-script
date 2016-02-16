from Naked.toolshed.shell import execute_js

# success case
series_a = execute_js('scripts/series-a.js')
series_b = execute_js('scripts/series-b.js')
series_c = execute_js('scripts/series-c.js')

print 'All scripts are done!'

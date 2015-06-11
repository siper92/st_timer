# Stack trace time measurement utility
PHP execution measurement utility that uses the xdebug stack trace 

#### Features
 * Measure times that a function took to execute and show the slowest functions
 * Show memory usage per function

# Setup configuration
```php
$dumpDir = dirname(__FILE__);   
ini_set('xdebug.trace_output_dir', $dumpDir);  
ini_set('xdebug.trace_format', 0);  
ini_set('xdebug.trace_format', 1);   
xdebug_start_trace();   

   # .... code to time

xdebug_stop_trace();  
```
OR

```php
// controls whether XDebug should collect the parameters passed to functions
//      3 -> Function variables with content
ini_set('xdebug.collect_params', 3);
// Controls whether XDebug should write the return value of function calls to the trace files.
// ini_set('xdebug.collect_return', 1); // breaks the store
ini_set('xdebug.trace_format', 1); // format of the dumped file
ini_set('xdebug.var_display_max_children', 0);
ini_set('xdebug.var_display_max_data', 100);
ini_set('xdebug.var_display_max_depth', 1);
$microtime = microtime(true);  // start time
xdebug_start_trace('stack_trace'.$microtime);

   # .... code to time

xdebug_stop_trace(); 
```


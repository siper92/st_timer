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

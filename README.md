# Stack trace time measurement utility
PHP execution measurement utility that uses the xdebug stack trace 

# Setup configuration
```
$dumpDir = dirname(__FILE__);   
ini_set('xdebug.trace_output_dir', $dumpDir);  
//ini_set('xdebug.xdebug.trace_format', '0');  
ini_set('xdebug.xdebug.trace_format', '1');   
xdebug_start_trace();   
.... code to time
xdebug_stop_trace();  
```

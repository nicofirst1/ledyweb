## Content

This folder contains the standard apache files which are required to run ledyweb on the rpi as a web server. 

Please do not modify the files by hand, use the [apache script](../../scripts/apache.sh) to change them and start the web server.



## Issues
If you are having problems with permissions add `umask 001` in `/etc/init.d/apache2`


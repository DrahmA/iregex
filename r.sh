#!/bin/sh

kill `pgrep -f "index.py"`  
spawn-fcgi -d ./ -f ./index.py -a 127.0.0.1 -p 9002



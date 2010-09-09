#!/bin/sh

kill `pgrep -f "index.py"`> /dev/null
sleep 1
spawn-fcgi -d ./ -f ./index.py -a 127.0.0.1 -p 9000



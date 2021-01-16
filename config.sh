#!/bin/bash

crontab -l | grep -q 'search string'  && echo 'entry exists' || echo 'entry does not exist'

(crontab -l 2>/dev/null; echo "*/5 * * * * /path/to/job -with args") | crontab -


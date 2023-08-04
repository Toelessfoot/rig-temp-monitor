#!/bin/bash

curr_date=$(date +%m%d%H%M)
crontab -l -u user > mycronBACKUP$curr_date
echo "@reboot python3 /rig-temp-monitor/rig-temp-monitor.py" > mycron
crontab -u user mycron
rm mycron

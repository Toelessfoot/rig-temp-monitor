#!/bin/bash

curr_date=$(date +%m%d%H%M)
crontab -l -u user > mycronBACKUP$curr_date
echo "@reboot unbuffer python3 /home/user/rig-temp-monitor/rig-temp-monitor.py >> /home/user/rig-temp-monitor.log 2>&1" > mycron
crontab -u user mycron
rm mycron

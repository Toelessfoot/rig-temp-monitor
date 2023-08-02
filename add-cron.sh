#!/bin/bash

curr_date=$(date +%m%d%H%M)

crontab -l > mycron
crontab -l > /cronBackups/mycronBACKUP$curr_date
echo "@reboot sleep 120 && python3 /rig-temp-monitor/rig-temp-monitor.py" >> mycron
crontab mycron
rm mycron

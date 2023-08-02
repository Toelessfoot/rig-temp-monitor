#!/bin/bash

crontab=$(crontab -l)
search="rig-temp-monitor"

if [[ "$crontab" == *"$search"* ]]; then
    echo "It's there."
else
    echo "It's not there. Adding it to cron"
    curr_date=$(date +%m%d%H%M)
    crontab -l -u user > mycron
    crontab -l -u user > mycronBACKUP$curr_date
    echo "@reboot python3 /rig-temp-monitor/rig-temp-monitor.py" >> mycron
    crontab -u user mycron
    rm mycron
fi

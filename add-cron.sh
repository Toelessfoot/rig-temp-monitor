#!/bin/bash

crontab -l > mycron
echo "@reboot sleep 120 && python3 /rig-temp-monitor/rig-temp-monitor.py" >> mycron
crontab mycron
rm mycron

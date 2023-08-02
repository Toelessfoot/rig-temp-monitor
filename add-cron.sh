#!/bin/bash

crontab -l > mycron
echo "@reboot python3 /rig-temp-monitor/rig-temp-monitor.py" >> mycron
crontab mycron
rm mycron

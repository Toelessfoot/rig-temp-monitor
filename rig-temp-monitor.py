from time import sleep
import subprocess
import re
from sys import argv
import os
import requests
from random import randrange

def send_telegram_msg(msg):
    data = {
        'text': msg,
        'chat_id': '-795504579'
    }
    try:
        req = requests.post(tele_url, data=data)
        print(req)
        print(req.text)
    except:
        print("Telegram message failed to send")

#get script directory and change cwd to it
print(f'Current Working Path: {os.getcwd()}')
script_dir = os.path.dirname(os.path.abspath(argv[0]))
print(f'Changing cwd to: {script_dir}')
os.chdir(script_dir)

hostname = subprocess.check_output("hostname", shell=True, encoding='utf-8').strip()

#get Telegram key
with open("data/tele.txt", "r") as f:
    token = f.read().strip()
tele_url = f'https://api.telegram.org/bot{token}/sendMessage'

#initial delay
sleep(20)
send_telegram_msg(f'{hostname} booted')
sleep(600)

minute = 60
hour = minute * 60
timeout = 2 * hour + randrange(hour)
timeout_min = timeout / 60

while True:
    #temperature limit
    with open("data/limit.txt", "r") as f:
        limit = int(f.read())

    if limit >= 72:
        print(f'Limit is: {str(limit)}')

        #toggle in file turns on or off
        with open("data/toggle.txt", "r") as f:
            toggle = f.read()
            toggle = toggle.strip()
            print(f'Toggle is: {toggle}')
            if toggle == "on":
                print("LIMIT ON")

                try:
                    out = subprocess.check_output("nvidia-smi", shell=True, encoding='utf-8')
                    reg = re.findall("\d{2,3}(?=C)", out)
                    for i in reg:
                        print(i)
                        if int(i) > limit:
                            print("HIGH")
                            send_telegram_msg(f"{hostname} - HIGH TEMPS shutting down for {timeout_min} min")
                            subprocess.run(f"sudo /hive/sbin/sreboot wakealarm {timeout}", shell=True)
                            exit()
                except:
                    print("An error occured with SMI")
    else:
        print("limit is too low")
    sleep(30)


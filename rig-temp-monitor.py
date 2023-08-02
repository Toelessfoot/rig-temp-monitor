from time import sleep
import subprocess
import re
from sys import argv
import os
import requests
from random import randrange

minute = 60
hour = minute * 60
timeout = 1 * hour + randrange(1 * hour)
timeout_min = timeout / 60

def send_telegram_msg(msg):
    print(msg)
    data = {
        'text': msg,
        'chat_id': '-795504579'
    }
    req = requests.post(tele_url, data=data)
    print(req)
    print(req.text)

#get script directory and change cwd to it
print(f'Current Working Path: {os.getcwd()}')
script_dir = os.path.dirname(os.path.abspath(argv[0]))
print(f'Changing cwd to: {script_dir}')
os.chdir(script_dir)

hostname = subprocess.check_output("hostname", shell=True, encoding='utf-8').strip()
print(hostname)

#get Telegram key
with open("data/tele.txt", "r") as f:
    token = f.read().strip()

tele_url = f'https://api.telegram.org/bot{token}/sendMessage'
print(tele_url)

while True:
    #temperature limit
    with open("data/limit.txt", "r") as f:
        limit = int(f.read())

    print(f'Limit is: {str(limit)}')

    #toggle in file turns on or off
    with open("data/toggle.txt", "r") as f:
        toggle = f.read()
        toggle = toggle.strip()
        print(f'Toggle is: {toggle}')
        if toggle == "on":
            print("LIMIT ON")

            out = subprocess.check_output("nvidia-smi", shell=True, encoding='utf-8')
            #with open("nvidia-smi.txt", "r") as f:
            #    out = f.read()

            reg = re.findall("\d{2,3}(?=C)", out)

            for i in reg:
                print(i)
                if int(i) > limit:
                    print("HIGH")
                    send_telegram_msg(f"{hostname} - HIGH TEMPS shutting down for {timeout_min} min")
                    subprocess.run(f"sreboot wakealarm {timeout}")
                    exit()
    sleep(30)


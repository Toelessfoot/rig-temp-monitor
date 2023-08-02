from time import sleep
import subprocess
import re
from sys import argv
import os

#get script directory and change cwd to it
print(f'Current Working Path: {os.getcwd()}')
script_dir = os.path.dirname(os.path.abspath(argv[0]))
print(f'Changing cwd to: {script_dir}')
os.chdir(script_dir)

while True:
    with open("limit.txt", "r") as f:
        limit = int(f.read())

    print(f'Limit is: {str(limit)}')

    with open("toggle.txt", "r") as f:                                                                                                     
        toggle = f.read()                                                                                                              
        toggle = toggle.strip()                                                                                                        
        print(f'Toggle is: {toggle}')                                                                                                                  
        if toggle == "on":                                                                                                             
            print("LIMIT ON")                                                                                                      
                                                                                                                                           
            #out = subprocess.check_output("nvidia-smi", shell=True, encoding='utf-8')                                                      
            with open("nvidia-smi.txt", "r") as f:
                out = f.read()
                                                                                                                                           
            reg = re.findall("\d{2,3}(?=C)", out)                                                                                          
                                                                                                                                           
            for i in reg:                                                                                                                  
                print(i)                                                                                                               
                if int(i) > limit:                                                                                                        
                    print("HIGH")                                                                                                  
        sleep(30)                                                                                                                      
                                 

#!/bin/python3
import os
import sys
import re
import shelve
import subprocess
import time
#sys.path.append("..")
from pyFunc import moduleSys


def biosNameCheck():
    biosN = subprocess.check_output(
            "sudo dmidecode -s baseboard-product-name", shell=True)
    biosN = str(biosN).lstrip('b\'').split('\\n')[0]
    return biosN 


def biFuncCheck():
    biosN = subprocess.check_output(
            "sudo dmidecode -s baseboard-product-name", shell=True)
    biosN = str(biosN).lstrip('b\'').split('\\n')[0]
    print(biosN)
    if re.search("V([0-9]C)", biosN):
        return "BI-120M-COM1"
    else:
        return "BI-120M"

def getCpuTemp():
    sensors = subprocess.check_output(
            "sensors -u", shell=True) 
    sensors = sensors.decode().splitlines()
    for line in sensors:
        if re.search('temp2_input', line):
            cpuT = str(f'{line}').split(':')[1]
            cpuT = int(float(cpuT))
#            print("cpuT is:", cpuT)
    return cpuT

def getCpuMips():
    with open('/proc/cpuinfo', 'r') as infos:
        for line in infos:
            if line.lower().startswith('bogomips'):
                mips = line.split(':')[1].lstrip().split('\n')[0]
        mips = int(float(mips))//100
        return mips

def getcpuH():
    if biosNameCheck() == "conga-QA5" or getCpuMips() >= 40:
        cpuH = 85
    else:
        cpuH = getCpuMips() + 33
    return cpuH

print("highTemp is:", cpuH)

def biStress():
    biTotal = 12
    biCount = 0
    #epoch time
    biTime = int(time.time())
    biEnd = int(time.time() + 10)
    
    cpuL = "20"
#    cpuH = getCpuMips() + 33
    #-c N, --cpu N start N workers spinning on sqrt(rand())
    #-m N, --vm N start N workers spinning on anonymous mma
    #-t N, --timeout T timeout after T seconds
    subprocess.call(
            "sudo stress-ng -c 4 -m 1 -l 80 -t 120m &", shell=True)    
    
    while biTime < biEnd:
        os.system('clear')
        biTime = int(time.time())
        cpuT = getCpuTemp()
        print("BI run %s, Total run 12 times" % biCount)
        print("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
        print("start time:", biTime)
        print("end time:", biEnd)
        time.sleep(1)


       


### Stript start here ###




with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

modelName = biosNameCheck()
mips = getCpuMips()
print(modelName)
print("mips: ", mips)
#moduleSys.snGet(pn, modelName)
getCpuTemp()

biStart = int(time.time())
biEnd = int(time.time() + 600)

biStress()
print("test done")

#!/bin/python3
import sys
import re
import shelve
import subprocess
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
   # sensors = sensors.split()
    print(sensors)
    for line in sensors:
        if line.find("temp1_input"):
            print(line)
    #    items = re.findall("temp1_input")

#    if "temp1_input" in sensors:

    #for line in sensors:
    #    if line.find('temp1_input'):
    #        print(line)
#    cpuT = sensors.find('temp1_input')
        #if re.search('temp1_input', sensors):

#            cpuT = line.split(':')[1].lstrip().split('\n')[0]
#    print("cpuT: ", cpuT)

def getCpuMips():
    with open('/proc/cpuinfo', 'r') as infos:
        for line in infos:
            if line.lower().startswith('bogomips'):
                mips = line.split(':')[1].lstrip().split('\n')[0]
        mips = int(float(mips))//100
        return mips

if biosNameCheck() == "conga-QA5" or getCpuMips() >= 40:
    highLimit = 85
else:
    highLimit = getCpuMips() + 33
print("high: ", highLimit)

with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

modelName = biosNameCheck()
mips = getCpuMips()
print(modelName)
print("mips: ", mips)
#moduleSys.snGet(pn, modelName)
getCpuTemp()
print("test done")

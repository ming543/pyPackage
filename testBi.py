#!/bin/python3
import os
import sys
import logging
import re
import shelve
import subprocess
import time
import json
from colorama import Fore, Back, Style
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
    #sensor -j > json type
    sensors = subprocess.check_output(
            "sensors -j", shell=True) 
    sensors = json.loads(sensors)
    cpuT = sensors['coretemp-isa-0000']['Core 0']['temp2_input']
    cpuT = int(float(cpuT))
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


def serialTest():
    #if modelName == "BI-120M-COM1":
    if biosNameCheck() == "V2C" or "V3C":
        serialTest = subprocess.call(
                "sudo /home/stux/tools/serial-test -p /dev/ttyS0 -b 115200 -o 1 -i 3", shell=True)
        if serialTest != 0:
            logging.error("RS232 serial loop test fail code:%s" % serialTest)
            moduleSys.failRed("RS232 serial loop test fail code:%s" % serialTest)
        else:
            logging.info("RS232 serial loop test pass code:%s" % serialTest)


def biStress():
    biTotal = 12
    biCount = 0
    cpuH = getcpuH()    
    cpuL = 20
    #-c N, --cpu N start N workers spinning on sqrt(rand())
    #-m N, --vm N start N workers spinning on anonymous mma
    #-t N, --timeout T timeout after T seconds
    subprocess.call(
            "sudo stress-ng -c 4 -m 1 -l 80 -t 120m &", shell=True)    
    serialTest()
    while biCount <= biTotal:
        nowTime = int(time.time())
        endTime = int(time.time() + 600)
        while nowTime < endTime:
            cpuT = getCpuTemp()
            if cpuL < cpuT < cpuH:
                os.system('clear')
                nowTime = int(time.time())
                print(" ")
                print("Test PN:%s SN:%s" % (pn, sn))
                print("BI run %s, Total run 12 times" % biCount)
                print("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
                print(" ")
                print("BI run %s Time End:" % biCount, time.ctime(endTime))
                print("BI run %s Time Now:" % biCount, time.ctime(nowTime))
                time.sleep(1)              
            else:
                print("TempHigh")
                logging.error("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
                moduleSys.failRed("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
        serialTest()
        biCount = biCount + 1
        logging.info("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))

    if biCount < biTotal:
        print("bicountFail", biCount)
        logging.error('Check BI total run %s failed!' % biCount)
        moduleSys.failRed('Check BI total run %s failed!' % biCount)
    else:
        print("bicount OK", biCount)
        logging.info('Check BI total run %s passed!' % biCount)



def biStressRoom():
    cpuL = 20
    if biosNameCheck() == "conga-QA5" or getCpuMips() >= 40:
        cpuH = 65
    else:
        cpuH = getCpuMips() + 15
    serialTest()
    subprocess.call(
            "sudo stress-ng -c 4 -m 1 -l 80 -t 120m &", shell=True)    
    nowTime = int(time.time())
    endTime = int(time.time() + 600)
    while nowTime < endTime:
        cpuT = getCpuTemp()
        if cpuL < cpuT < cpuH:
            os.system('clear')
            nowTime = int(time.time())
            print(" ")
            print(Fore.BLUE + Back.WHITE)
            print("燒機測試 BI Test")
            print(Fore.MAGENTA + Back.WHITE)
            print("Test PN:%s SN:%s" % (pn, sn))
            print("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
            print(Style.RESET_ALL)
            print(" ")
            print("結束時間 BI Time End:", time.ctime(endTime))
            print("現在時間 BI Time Now:", time.ctime(nowTime))
            time.sleep(1)              
        else:
            print("CPU 溫度過高 TempHigh")
            logging.error("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
            moduleSys.failRed("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
    serialTest()
    logging.info("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))


### Stript start here ###
os.system('clear')
with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']
modelName = biFuncCheck()
sn = moduleSys.snGet(pn, modelName)
biStress()
#biStressRoom()
print("test done")
moduleSys.passGreen()


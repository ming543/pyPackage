#!/bin/python3
import git
import os
import sys
import logging
import shelve
import getmac
import time
# import datetime
import re
import subprocess
import enquiries
import cpuinfo
import netifaces
import serial
from colorama import Fore
import pexpect

pyFolder = "/home/stux/pyPackage/"
ekitFolder = pyFolder + "tools/EKit_L"

def aicVersion():
#    output = getattr(sys.stdout, 'buffer', sys.stdout)
#    logfile = output
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
#    time.sleep(1)
    process.expect('( 1)*') #System Info
    process.sendline("1\r")
    process.expect("( 1)*") #Firmware Info
    process.sendline("1\r")
    process.expect("(Exit)*") #Firmware Info
    process.sendline("exit\r")
    time.sleep(1)
    process.expect(pexpect.EOF)
    result = process.before
#    print(result)

#    process.logfile = sys.stdout.decode('utf-8') 
#    print(process.readline())
#    aicV = process.readline()
#    print(aicV)
    if re.search("AIC-1.02", result):
        print("AICOK: "  )
    else:
        print("AICNG: " )

#    process.expect(pexpect.EOF)
#    print(process.before)
#    print(process.expect(pexpect.EOF))

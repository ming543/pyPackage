#!/bin/python3
import os
import sys
import logging
import re
import shelve
import subprocess
import enquiries
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

def storageGet():
    output = subprocess.check_output(
            'lsblk -o type,path,model,size', shell=True)
    output = str(output).lstrip('b\'').split('\\n')
    options = []
    for line in output:
        if line.lower().startswith('disk'):
            options.append(line)
    choice = enquiries.choose(' Choose clone disk options: ', options)
    diskGet = choice.split(' ')[1]
#    print('diskinfo:', options)
#    print('diskget', diskGet)
    return diskGet

### Stript start here ###

with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']
modelName = biFuncCheck()
#sn = moduleSys.snGet(pn, modelName)
storageGet()
print("test done")

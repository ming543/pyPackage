#!/bin/python3
import sys
import shelve
sys.path.append("..")
from pyFunc import moduleSys

if moduleSys.biFuncCheck() is True:
    modelName = "BI-120M-COM1"
else:
    modelName = "BI-120M"

with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']
print(pn) 
moduleSys.snGet(pn, modelName)
moduleSys.rtcCheck()
moduleSys.cpuInfo()

print("test done")

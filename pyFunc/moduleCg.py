#!/bin/python3
import os
import getmac
import cgos as cg
cg.openif()
result = cg.boardGetInfo()
print (result)
print (result['szSerialNumber'])

pyFolder = "/home/stux/pyPackage/"
cgFolder = pyFolder + "tools/CgosPy_1_2"

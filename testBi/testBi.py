#!/bin/python3
import sys
sys.path.append("..")
from pyFunc import moduleSys

modelName = "BI-120M"
pn = moduleSys.pnGet()

moduleSys.snGet(pn, modelName)
moduleSys.rtcCheck()
moduleSys.cpuInfo()
moduleSys.dmidecodeCheck("baseboard-product-name", "V3C")
moduleSys.dmidecodeCheck("baseboard-product-name", "V2C")


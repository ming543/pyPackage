#!/bin/python3
import os
import shelve
import inspect
import subprocess
from colorama import Fore
from pyFunc import moduleSys
from pyFunc import moduleEbk
from pyFunc import moduleCg

startTest = "/home/stux/pyPackage/t.sh"
#Get PN from db
with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

def AIM(sCPU, sPoe, sFan, sDio, sLan, sCom):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2019")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    moduleEbk.aicPoe(sPoe)
#    moduleEbk.aicFan(sFan)
    moduleEbk.aicDioSelect(sDio)
    moduleSys.rtcCheck()
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageGet()
    for i in range(sLan):
        moduleSys.lanCheck("eth%s" % i, "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    #moduleSys.uartLoopCheck("/dev/ttyS0", "1")
    for i in range(sCom):
        j = i + 1
        moduleSys.uartLoopCheck("/dev/ttyS%s" % i, "%s" % j)
    moduleSys.alsabatTest()


def AIH(sCPU, sPoe, sFan, sDio, sLan, sCom):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2020")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    moduleEbk.aicPoe(sPoe)
    moduleEbk.aicFan(sFan)
    moduleEbk.aicDioSelect(sDio)
    moduleSys.rtcCheck()
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageGet()
    for i in range(sLan):
        moduleSys.lanCheck("eth%s" % i, "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    moduleSys.uartLoopCheck(sCom)
    moduleSys.alsabatTest()

def Q715QA5(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck()
#    moduleSys.cpuGet()
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.lanSpeedSet(2, 100)
    moduleSys.lanLedCheck("綠", "橘")
    moduleSys.lanLedOffCheck("滅", "滅")
    moduleSys.usbCheck("Keyboard|Holtek", 1)
    moduleSys.usbCheck("JMS567", 1)
    #SIM7600
    moduleSys.atCheck("/dev/ttyUSB2", "ati", "Rev")
    moduleSys.atCheck("/dev/ttyUSB2", "ati", "IMEI")
    moduleSys.atCheck("/dev/ttyUSB2", "at+cgmr", "CGMR")
    moduleSys.atCheck("/dev/ttyUSB2", "at+ciccid", "ICCID")
    #EC25
#    moduleSys.atCheck("/dev/ttyUSB2", "ati", "Rev")
#    moduleSys.atCheck("/dev/ttyUSB2", "at+qccid", "CCID")
    moduleSys.cpuTempCheck(20, 60)

def U7130PAS():
    print("Not Ready")

def U713064G():
    print("Not Ready")

def U7130(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck()
#    moduleSys.cpuGet()
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.usbCheck("Keyboard|Holtek", 1)
    moduleSys.usbCheck("Mouse", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleCg.i2cGpio()
    moduleSys.uartLoop("/dev/ttyS0")
    moduleSys.aplayTest()
    moduleSys.arecordTest()
    moduleSys.cpuTempCheck(20, 60)

def U7150(sCPU):
    print("Not Ready")

def U6500(sCPU):
    print("Not Ready")


def default():
    print("此PN無對應測試程式")
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)


def debug(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.cpuCheck(sCPU)
    

os.system('clear')
print(Fore.YELLOW + "組裝測試選單 ASSY-MENU" + Fore.RESET, end='')
print(" Build by EFCO SamLee")
print("測試PN:", pn)

#DIO=GPIO1 IDIO=DIO1
#1-CPU, Poe, fan, dio, Lan, Com
if pn == "10300-000000-A.0": debug("NA")
elif pn == "10300-000004-A.3": Q715QA5("NA")
elif pn == "10300-000004-A.4": Q715QA5("NA")
elif pn == "10300-000007-A.0": Q715QA5("NA")
elif pn == "10400-000004-B.2": U7130PAS("NA")
elif pn == "10400-000009-A.0": U7150("NA")
elif pn == "10400-000010-A.0": U7150("NA")
elif pn == "10500-000340-A.0": U713064G("NA")
elif pn == "10902-000097-A.0": AIM("6300", 4, "noFan", "DIO1", 4, 4)
elif pn == "10951-000004-A.0": U7130("NA")
elif pn == "10953-000001-B.0": U650("NA")
elif pn == "20010-000160-A.0": AIM("6600", 4, "noFan", "1I", 4, 4)
elif pn == "20010-000161-A.0": AIM("6300", 4, "noFan", "1I", 4, 4)
elif pn == "20010-000162-A.0": AIM("6100", 4, "noFan", "1I", 4, 4)
elif pn == "20010-000170-A.0": AIH("NA", 4, 2, "1D2D", 6, 2)
elif pn == "20010-000173-A.1": AIM("6600", 0, "noFan", "1I", 2, 4) #AIML-I
elif pn == "20010-000177-A.1": AIM("6300", 0, "noFan", "1I", 2, 4) #AIML-I
elif pn == "20010-000179-A.1": AIM("3955", 0, "noFan", "1I", 2, 4) #AIML-I
elif pn == "20010-000181-A.2": AIH("NA", 4, 2, "1I2I", 6, 2) #AIHDP-i2
elif pn == "20010-000191-A.1": AIM("7300", 0, "noFan", "1I", 2, 4) #AIML-I
elif pn == "20010-000194-A.2": AIH("NA", 4, "noFan", "1D", 6, 6) #AIH-DIO
elif pn == "20010-000197-A.1": AIH("NA", 4, 2, "1D", 6, 6) #AIH-EP1
elif pn == "20010-000199-A.1": AIH("NA", 4, 2, "1I2D", 6, 2) #AIHDP-i
elif pn == "20010-000335-A.0": U7130("NA")
elif pn == "10300-000001-A.0": AIH("", 4, 2, "1I2I", 6, 2) #1-Poe 2-fan, 3-dio, 4-Lan, 5-Com
else: default()

moduleSys.passGreen()

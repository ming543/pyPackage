#!/bin/python3
import os
import shelve
import inspect
import subprocess
from colorama import Fore
from pyFunc import moduleSys
from pyFunc import moduleEbk

startTest = "/home/stux/pyPackage/t.sh"
#Get PN from db
with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

def AIM(sPoe, sFan, sDio, sLan, sCom):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2019")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    if sPoe == 4:
        for i in range(1, sPoe + 1):
            moduleEbk.aicPoe("PoE  %s Present:" % i)
#    moduleEbk.aicPoe("PoE  1 Present:")
#    moduleEbk.aicFan("Fan 1 RPM:")
#    moduleEbk.aicFan("Fan 2 RPM:")
    moduleEbk.aicDio(sDio, 00)
    moduleSys.rtcCheck()
    moduleSys.cpuGet()
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


def AIH(sPoe, sFan, sDio, sLan, sCom):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2020")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    for i in range(1, sPoe + 1):
        moduleEbk.aicPoe("PoE  %s Present:" % i)
    if sFan == "2Fan":
        moduleEbk.aicFan("Fan 1 RPM:")
        moduleEbk.aicFan("Fan 2 RPM:")
    if sDio == "1D2D":
        moduleEbk.aicDio("GPIO1", 00)
        moduleEbk.aicDio("GPIO2", 00)
    elif sDio == "1I2D":
        moduleEbk.aicDio("DIO1", 00)
        moduleEbk.aicDio("GPIO2", 00)
    elif sDio == "1I2I":
        moduleEbk.aicDio("DIO1", 00)
        moduleEbk.aicDio("DIO2", 00)
    elif sDio == "1I":
        moduleEbk.aicDio("DIO1", 00)
    elif sDio == "1D":
        moduleEbk.aicDio("GPIO1", 00)
    moduleSys.rtcCheck()
    moduleSys.cpuGet()
    moduleSys.memoryGet()
    moduleSys.storageGet()
    for i in range(sLan):
        moduleSys.lanCheck("eth%s" % i, "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    for i in range(sCom):
        j = i + 1
        moduleSys.uartLoopCheck("/dev/ttyS%s" % i, "%s" % j)

def Q715QA5():
    print("Not Ready")

def U7130PAS():
    print("Not Ready")

def U713064G():
    print("Not Ready")

def U7130():
    print("Not Ready")

def U7150():
    print("Not Ready")

def U6500():
    print("Not Ready")


def default():
    print("此PN無對應測試程式")
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)


os.system('clear')
print(Fore.YELLOW + "組裝測試選單 ASSY-MENU" + Fore.RESET, end='')
print(" Build by EFCO SamLee")
print("測試PN:", pn)

#DIO=GPIO1 IDIO=DIO1
#1-Poe 2-fan, 3-dio, 4-Lan, 5-Com
if pn == "10300-000004-A.3": Q715QA5()
elif pn == "10300-000004-A.3": Q715QA5()
elif pn == "10300-000004-A.4": Q715QA5()
elif pn == "10300-000007-A.0": Q715QA5()
elif pn == "10400-000004-B.2": U7130PAS()
elif pn == "10400-000009-A.0": U7150()
elif pn == "10400-000010-A.0": U7150()
elif pn == "10500-000340-A.0": U713064G()
elif pn == "10902-000097-A.0": AIM(4, "noFan", "DIO1", 4, 4)
elif pn == "10951-000004-A.0": U7130()
elif pn == "10953-000001-B.0": U650()
elif pn == "20010-000160-A.0": AIM(4, "noFan", "DIO1", 4, 4)
elif pn == "20010-000161-A.0": AIM(4, "noFan", "DIO1", 4, 4)
elif pn == "20010-000162-A.0": AIM(4, "noFan", "DIO1", 4, 4)
elif pn == "20010-000170-A.0": AIH(4, "2Fan", "1D2D", 6, 2)
elif pn == "20010-000173-A.1": AIM(0, "noFan", "DIO1", 2, 4) #AIML-I
elif pn == "20010-000177-A.1": AIM(0, "noFan", "DIO1", 2, 4) #AIML-I
elif pn == "20010-000179-A.1": AIM(0, "noFan", "DIO1", 2, 4) #AIML-I
elif pn == "20010-000181-A.2": AIH(4, "2Fan", "1I2I", 6, 2) #AIHDP-i2
elif pn == "20010-000191-A.1": AIM(0, "noFan", "DIO1", 2, 4) #AIML-I
elif pn == "20010-000194-A.2": AIH(4, "noFan", "1D", 6, 6) #AIH-DIO
elif pn == "20010-000197-A.1": AIH(4, "2Fan", "1D", 6, 6) #AIH-EP1
elif pn == "20010-000199-A.1": AIH(4, "2Fan", "1I2D", 6, 2) #AIHDP-i
elif pn == "10300-000000-A.0": AIH(4, "2Fan", "1I2I", 6, 2) #1-Poe 2-fan, 3-dio, 4-Lan, 5-Com
else: default()

moduleSys.passGreen()

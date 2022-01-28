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

def AIM(IO1):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2019")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    moduleEbk.aicPoe("PoE  1 Present:")
    moduleEbk.aicPoe("PoE  2 Present:")
    moduleEbk.aicPoe("PoE  3 Present:")
    moduleEbk.aicPoe("PoE  4 Present:")
#    moduleEbk.aicFan("Fan 1 RPM:")
#    moduleEbk.aicFan("Fan 2 RPM:")
#DIO1=GPIO1 IDIO1=DIO1
    moduleEbk.aicDio(IO1, 00)
    moduleSys.rtcCheck()
    moduleSys.cpuGet()
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.lanCheck("eth1", "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    moduleSys.uartLoopCheck("/dev/ttyS0", "1")

def AIML():
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2019")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
#    moduleEbk.aicFan("Fan 1 RPM:")
#    moduleEbk.aicFan("Fan 2 RPM:")
    moduleEbk.aicDio("GPIO1", 00)
    moduleSys.rtcCheck()
    moduleSys.cpuGet()
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.lanCheck("eth1", "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    moduleSys.uartLoopCheck("/dev/ttyS0", "1")

def AIHD(sFan, sDio):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2020")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
#    moduleEbk.aicPoe("PoE  1 Present:")
#    moduleEbk.aicPoe("PoE  2 Present:")
#    moduleEbk.aicPoe("PoE  3 Present:")
#    moduleEbk.aicPoe("PoE  4 Present:")
    if sFan == "0":
        print("No Fan")
    else sFan == "2":
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

    moduleSys.rtcCheck()
    moduleSys.cpuGet()
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.lanCheck("eth1", "80:7b:85")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("hub", 3)
    moduleSys.uartLoopCheck("/dev/ttyS0", "1")

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

if pn == "10300-000004-A.3": Q715QA5()
elif pn == "10300-000004-A.3": Q715QA5()
elif pn == "10300-000004-A.4": Q715QA5()
elif pn == "10300-000007-A.0": Q715QA5()
elif pn == "10400-000004-B.2": U7130PAS()
elif pn == "10400-000009-A.0": U7150()
elif pn == "10400-000010-A.0": U7150()
elif pn == "10500-000340-A.0": U713064G()
elif pn == "10902-000097-A.0": AIM("DIO1")
elif pn == "10951-000004-A.0": U7130()
elif pn == "10953-000001-B.0": U650()
elif pn == "20010-000160-A.0": AIM("DIO1")
elif pn == "20010-000161-A.0": AIM("DIO1")
elif pn == "20010-000162-A.0": AIM("DIO1")
elif pn == "10300-000000-A.0": AIHD("0","1I2I") #1-fan, 2-dio
else: default()

moduleSys.passGreen()

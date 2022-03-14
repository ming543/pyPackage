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


def IOM2GR(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def IOMH4GR(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def Q715VT2(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.lanSpeedSet(2, 100)
    moduleSys.lanLedCheck("綠", "橘")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("JMS567", 1)
    #SIM7600
    moduleSys.atCheck("/dev/ttyUSB2", "ati", "Rev")
    moduleSys.atCheck("/dev/ttyUSB2", "ati", "IMEI")
    moduleSys.atCheck("/dev/ttyUSB2", "at+cgmr", "CGMR")
    moduleSys.atCheck("/dev/ttyUSB2", "at+ciccid", "ICCID")


def Q718B(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def Q718PAS(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")
  
def V2C(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def V2CE(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def V2CL(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    print("Not Ready")

def debug(sCPU):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.cpuCheck(sCPU)

def default():
    print("此PN無對應測試程式")
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)


os.system('clear')
print(Fore.YELLOW + "PCBA測試選單 PCBA-MENU" + Fore.RESET, end='')
print(" Build by EFCO SamLee")
print("測試PN:", pn)

#DIO=GPIO1 IDIO=DIO1
#1-CPU, Poe, fan, dio, Lan, Com
if pn == "10300-000000-A.0": debug("NA")
elif pn == "20030-000020-A.1": Q715VT2("NA")
elif pn == "20040-000049-A.1": V2CL("7600")
elif pn == "20040-000050-A.1": V2CL("7300")
elif pn == "20040-000051-A.1": V2CL("7100")
elif pn == "20070-000412-2.2": Q718B("NA")
elif pn == "20070-000519-A.0": Q718PAS("NA")
elif pn == "20070-000556-A.3": V2C("6600")
elif pn == "20070-000557-A.3": V2C("6300")
elif pn == "20070-000558-A.3": V2C("6100")
elif pn == "20070-000568-A.1": IOM2GR("NA")
elif pn == "20070-000639-A.1": V2CE("6100")
elif pn == "20070-000675-A.1": IOMH4GR("NA")
else: default()

moduleSys.passGreen()

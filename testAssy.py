#!/bin/python3
import os
import shelve
import inspect
import subprocess
from colorama import Fore
from pyFunc import moduleSys

startTest = "/home/stux/pyPackage/t.sh"
#Get PN from db
with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

def AIML():
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.biosVersionCheck("1.20")
    moduleSys.rtcCheck()
    moduleSys.cpuGet()
    moduleSys.memoryGet()
    moduleSys.storageGet()
    moduleSys.macCheck("eth0", "80:7b:85")
    moduleSys.lanCarrierCheck("eth1")

def default():
    print("無對應組裝測試程式")
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)



switcher = {
    "10300-000000-A.0": AIML,
    7: AIML
    }

def switch(pnNum):
    return switcher.get(pnNum, default)()

os.system('clear')
print(Fore.YELLOW + "組裝測試選單 ASSY-MENU" + Fore.RESET, end='')
print(" Build by EFCO SamLee")
print("測試PN:", pn)

switch(pn)
moduleSys.passGreen()

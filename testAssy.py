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
    print("modelName: ", modelName)
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"

def default():

    print("無對應組裝測試程式")
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)



switcher = {
    "10953-000321-A.r12": AIML,
    "10300-000000-A.0": AIML,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(pnNum):
    return switcher.get(pnNum, default)()

os.system('clear')
print(Fore.YELLOW + "組裝測試選單 ASSY-MENU" + Fore.RESET, end='')
print(" Build by EFCO SamLee")
print("測試PN:", pn)
#sn = moduleSys.snGet(pn, modelName)
switch(pn)
#moduleSys.passGreen()

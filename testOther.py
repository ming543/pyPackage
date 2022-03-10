#coding: utf8
#!/bin/python3
import git
import os
import sh
import sys
import subprocess
import enquiries
import time
import shelve
import shutil
# import re
from colorama import Fore
from pyFunc import moduleSys

# start test file
startTest = "/home/stux/pyPackage/t.sh"

# Check system boot by UEFI or LEGACY mode
booted = "UEFI" if os.path.exists("/sys/firmware/efi") else "LEGACY"

# Get revision
g = git.Git('.')
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')


def mMenu():
    m0 = '返回主選單 BackToMain'
    m1 = '網路更新本機BIOS程式 Update local BIOS folder'
    m2 = '修復DOS開機 Fix MBR for DOS boot'
    options = [m0, m1, m2]

    os.system('clear')
    print(Fore.YELLOW + "%s 其他選單 OTHER-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("測試程式版本 Revision %s" % loginfo)
    choice = enquiries.choose(' 選擇測試項目 Choose options:', options)

    if choice == m0:  # pyMenu
        pyMenu()
    elif choice == m1:  # biosFolderUpdate
        biosFolderUpdate()
    elif choice == m2:  # fix MBR
        fixMbr()
    

def pyMenu():
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)


def biosFolderUpdate():
    scrConfig = '/home/stux/pyPackage/tools/rclone.conf'
    desConfig = '/home/stux/.config/rclone/rclone.conf'
    shutil.copyfile(scrConfig, desConfig)
    
    os.system('clear')
    rcloneFolder = "EFCO_test_script:/V23C_DOS/BIOS"
    localFolder = "/home/partimag/BIOS/"
    des = "/home/partimag/"
    response = subprocess.call(
            "rclone sync  %s %s -P" % (rcloneFolder, localFolder), shell=True)
    if response == 0:
        print("更新成功")
    else:
        print("更新失敗")
    input("按任意鍵繼續 Press any key continue...")

    scr = localFolder  + "*.nsh"
    subprocess.call("cp %s %s" %(scr, des), shell=True)
    mMenu()

def fixMbr():
    os.system('clear')
    ifFile = "/usr/lib/syslinux/mbr/mbr.bin"
    ofFile = "/dev/sda"
    response = subprocess.call(
        "sudo dd if=%s of=%s" % (ifFile, ofFile), shell=True)
    if response == 0:
        print("更新成功")
    else:
        print("更新失敗")
    input("按任意鍵繼續 Press any key continue...")
    mMenu()
    
mMenu()

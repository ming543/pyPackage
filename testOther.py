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
    m1 = '更新本機BIOS程式 Update local BIOS folder'
    m2 = '修復DOS開機 Fix MBR for DOS boot'
    m3 = '更新DOS測試程式 Update DOS Test Script'
    m4 = '更新本機UEFI程式'
    m5 = '確認功能 FT232H GPIO test'
    m6 = '更新本機zerotier address'
    options = [m0, m1, m2, m3, m4, m5, m6]

    os.system('clear')
    print(Fore.YELLOW + "%s 其他選單 OTHER-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee明")
    print("測試程式版本 Revision %s" % loginfo)
    choice = enquiries.choose(' 選擇測試項目 Choose options:', options)

    if choice == m0:  # pyMenu
        pyMenu()
    elif choice == m1:  # biosFolderUpdate
        biosFolderUpdate()
    elif choice == m2:  # fix MBR
        fixMbr()
    elif choice == m3:  # update DOS
        #moduleSys.dosPull()
        print("The Function not support now...")
        input("按任意鍵繼續 Press any key continue...")
        mMenu()
    elif choice == m4: # update UEFI tools
        uefiFolderUpdate()
    elif choice == m5:  # ft232Test
        ft232hCheck()
    elif choice == m6:  # update zerotier address
        zerotierUpdate()

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

def ft232hCheck():
    os.environ.setdefault('BLINKA_FT232H', '1')
    import board
    import digitalio
    C0 = digitalio.DigitalInOut(board.C0)
    C1 = digitalio.DigitalInOut(board.C1)
    C2 = digitalio.DigitalInOut(board.C2)
    C3 = digitalio.DigitalInOut(board.C3)
    C4 = digitalio.DigitalInOut(board.C4)
    C5 = digitalio.DigitalInOut(board.C5)
    C6 = digitalio.DigitalInOut(board.C6)
    C7 = digitalio.DigitalInOut(board.C7)
    for i in range(8):
        locals()['C' + str(i)].direction = digitalio.Direction.INPUT
    count = 0
    while count < 30:
        time.sleep(1)
        os.system('clear')
        startTime = time.strftime("%H%M%S", time.localtime())
        print('Check FT232H GPIO status... ' + startTime)
        for i in range(8):
            print('The GPIO Port %s: ' % i, end='' )
            print(str(locals()['C' + str(i)].value))

        count = count + 1
        print(' ')
        print('Test end at count 30, now is %s' % count)
    mMenu()


def zerotierUpdate():
    os.system('clear')
    print('Stop service zerotier ... ')
    response = subprocess.call(
            "sudo service zerotier-one stop", shell=True)
    time.sleep(5)
    print('Remove zerotier identity ... ')
    response = subprocess.call(
            "sudo rm /var/lib/zerotier-one/identity.public", shell=True)
    response = subprocess.call(
            "sudo rm /var/lib/zerotier-one/identity.secret", shell=True)
    print('Start service zerotier ... ')
    response = subprocess.call(
            "sudo service zerotier-one start", shell=True)
    time.sleep(5)
    response = subprocess.call(
            "sudo zerotier-cli info", shell=True)
    input("按任意鍵繼續 Press any key continue...")
    mMenu()




def uefiFolderUpdate():
    os.system('clear')
    scrFolder = "/home/stux/pyPackage/tools/uefi/."
    #desFolder = "/boot/efi"
    desFolder = "/boot/efi/."
    response = subprocess.call(
            "sudo scp -r %s %s" % (scrFolder, desFolder), shell=True)
    if response == 0:
        print("更新成功")
    else:
        print("更新失敗")
    input("按任意鍵繼續 Press any key continue...")
    mMenu()



mMenu()

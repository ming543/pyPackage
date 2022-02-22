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
# import shutil
# import re
from colorama import Fore
from pyFunc import moduleSys

# start test file
pyFolder = "/home/stux/pyPackage/"
startTest = pyFolder + "t.sh"

# Check system boot by UEFI or LEGACY mode
booted = "UEFI" if os.path.exists("/sys/firmware/efi") else "LEGACY"

# Get revision
g = git.Git('.')
dosFolder = "/usr/lib/live/mount/persistence/sda1/"
gDos = git.Git(dosFolder)
# loginfo = g.log('-p', '-1' , '--date=iso')
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')
#logDos = gDos.log('-m', '-1', '--pretty=format:"%h %s"')
# logData = loginfo.splitlines()
# rev = logData[2] + logData[4]
#Check and mount log folder
logFolder = "/home/partimag/log"
if os.path.isdir(logFolder):
    print("Logfolder exist")
else:
    subprocess.check_call("sudo mount /dev/sda2 /home/partimag -o umask=000", shell=True, stdin=sys.stdin)

#Get PN from db
with shelve.open(pyFolder + 'dataBase') as db:
    pn = db['pnSave']

def mMenu():
    m0 = '測試PN設定 PN-Setup'
    m1 = '組裝測試 Assy-Test (Label: SS02XXXX & CS04XXXX)'
    m2 = '板階測試 PCBA-Test (Label: 000168-A0-SB000XXX)'
    m3 = '其他測試 Other-Test'
    m4 = '燒機測試 BurnIn-Test'
    m5 = '作業系統安裝 OS Clone Setup'
    m6 = '網路上傳日誌檔 Copy Log to Onedrive'
    m7 = '更新本機測試程式 Update Test Script'
    m8 = '更新DOS測試程式 Update DOS Test Script'
    ml = '系統關機 Power off system'
    options = [m0, m1, m2, m3, m4, m5, m6, m7, m8, ml]

    os.system('clear')
    print(Fore.YELLOW + "%s 主選單 MAIN-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("測試程式版本 LINUX Revision %s" % loginfo)
    #print("測試程式版本 DOS Revision %s" % logDos)
    choice = enquiries.choose('PN:%s 選擇測試項目 Choose options:' % pn, options)

    if choice == m0:  # pn Setup
        pnMenu()
    elif choice == m1:  # Assy test
        aMenu()
    elif choice == m2:  # PCBA test
        pMenu()
    elif choice == m3:  # other test
        oMenu()
    elif choice == m4:  # Burnin test
        bMenu()
    elif choice == m5:  # OS clone setup
        osClone()
    elif choice == m6:  # copy log to onedrive
        copyLog()
    elif choice == m7:  # Update Linux script
        gitPull()
    elif choice == m8:  # Update Linux script
        dosPull()
    # Last of list
    elif choice == ml:  # power off system
        print("系統關機 The system will shutdown after 5 secs!")
        time.sleep(5)
        os.system('systemctl poweroff')


def pnMenu():
    os.system('clear')
    moduleSys.pnGet()
    moduleSys.pnCheck()
    sys.stdout.flush()
    os.execv(sys.executable, ["python3"] + sys.argv)


#AssyTest
def aMenu():
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 testAssy.py")
    subprocess.call("sh %s" % startTest, shell=True)
    

# Show all PN of testAssy
def aMenu2():
    os.system('clear')
    index = []
    aPath = pyFolder + "testAssy"
    print(Fore.YELLOW + "%s 組裝測試選單 ASSY-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    for filename in os.listdir(aPath):
        index += [filename]
    choice = enquiries.choose('  選擇測試項目 Choose options: ', index)
    for i in range(len(index)):
        if choice == index[i]:
            with open(startTest, "w") as f:
                f.write("cd " + aPath + "&& python3 %s" % index[i])
            print(index[i])
            subprocess.call("sh %s" % startTest, shell=True)

#pcbaTest
def pMenu():
    os.system('clear')
    p1 = 'p1'
    p2 = 'p2'
    pl = 'Back to MAIN-MENU'
    options = [p1, p2, pl]
    print(Fore.YELLOW + "%s PCBA-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    choice = enquiries.choose('  Choose options: ', options)
    if choice == p1:
        print("p1 is")
    elif choice == p2:
        print("p2 is")
    elif choice == pl:
        mMenu()

#otherTest
def oMenu():
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 testOther.py")
    subprocess.call("sh %s" % startTest, shell=True)


#biTest
def bMenu():
    os.system('clear')
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 testBi.py")
    subprocess.call("sh %s" % startTest, shell=True)


#osclone
def osClone():
    os.system('clear')
    moduleSys.diskGet()
    moduleSys.osGet()
    if moduleSys.cloneCheck() is True:
        with open(startTest, "w") as f:
            f.write("cd /home/stux/pyPackage && python3 osClone.py")
        subprocess.call("sh %s" % startTest, shell=True)
    else:
        mMenu()


#logToOnedrive
def copyLog():
    os.system('clear')
    for i in range(5):  # ping 5 times
        response = subprocess.call(
                "ping -c 1 -w 1 8.8.8.8", shell=True)
        print("response: ", response)
        time.sleep(2)
        if response == 0:
            print("PING OK")
            lF = "/home/partimag/log"
            oF = "onedrive:General/log"
            rC = subprocess.call("rclone -v copy %s %s -P" % (lF, oF), shell=True)
            if rC == 0:  # check rclone pass or fail
                print(Fore.GREEN + "日誌檔案上傳成功 Log copy to onedrive done!!!" + Fore.RESET)
                time.sleep(5)
                break
            else:
                print(Fore.RED + "日誌檔案上傳失敗 Log copy to onedrive Fail!!!" + Fore.RESET)
                time.sleep(5)
                break
        else:
            print(Fore.YELLOW + "外網測試失敗 Ping fail, check internet" + Fore.RESET)
            time.sleep(1)
    mMenu()


#linuxUpdate
def gitPull():
    os.system('clear')
    for i in range(5):  # ping 5 times
        response = subprocess.call(
                "ping -c 1 -w 1 8.8.8.8", shell=True)
        if response == 0:
            print("PING OK")
            g.gc()
            g.fetch('--all')
            g.reset('--hard')
            g.clean('-f', '-d')
            g.pull()
            print("gitPullDone")
            subprocess.call("cd %s && sh system.sh" % pyFolder, shell=True)
            time.sleep(3)
            break
        else:
            print(Fore.YELLOW + "外網測試失敗 Ping fail, check internet" + Fore.RESET)
            time.sleep(5)
    sys.stdout.flush()
    os.execv(sys.executable, ["python3"] + sys.argv)


#DOS Update 
def dosPull():   
    os.system('clear')
    for i in range(5):  # ping 5 times
        response = subprocess.call(
                "ping -c 1 -w 1 8.8.8.8", shell=True)
        if response == 0:
            print("PING OK")
            subprocess.call("cd %s && sudo git remote add origin https://github.com/ming543/V23C_DOS.git" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git fetch --all" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git checkout origin/master -- FDCONFIG.SYS" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git checkout origin/master -- FDAUTO.BAT" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git checkout origin/master -- V23C_FD" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git checkout origin/master -- AICCFG" % dosFolder, shell=True)
            subprocess.call("cd %s && sudo git checkout origin/master -- NC" % dosFolder, shell=True)
            print("gitDosPullDone")
            subprocess.call("cd %s && sh system_dos.sh" % pyFolder, shell=True)
            time.sleep(5)
            break
        else:
            print(Fore.YELLOW + "外網測試失敗 Ping fail, check internet" + Fore.RESET)
            time.sleep(5)
    sys.stdout.flush()
    os.execv(sys.executable, ["python3"] + sys.argv)


mMenu()

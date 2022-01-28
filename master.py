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
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')

#Check and mount log folder
logFolder = "/home/partimag/log"
if os.path.isdir(logFolder):
    print("Logfolder exist")
else:
    subprocess.check_call("sudo mount /dev/sda2 /home/partimag -o umask=000", shell=True, stdin=sys.stdin)

def mMenu():
    m0 = '製作測試碟64G Build test disk'
    m7 = '更新本機測試程式 Update Test Script'
    ml = '系統關機 Power off system'
    options = [m0, m7, ml]

    os.system('clear')
    print(Fore.YELLOW + "%s 主選單 MAIN-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("測試程式版本 Revision %s" % loginfo)
    choice = enquiries.choose(' 選擇測試項目 Choose options:', options)

    if choice == m0:  # Build test disk
        testerBuild()
    elif choice == m7:  # Update Linux script
        gitPull()
    # Last of list
    elif choice == ml:  # power off system
        print("系統關機 The system will shutdown after 5 secs!")
        time.sleep(5)
        os.system('systemctl poweroff')


#build test disk
def testerBuild():
    os.system('clear')
    output = subprocess.check_output(
            'lsblk -o type,name,model,size', shell=True)
    output = str(output).lstrip('b\'').split('\\n')
    options = []
    for line in output:
        if line.lower().startswith('disk'):
            options.append(line)
    print("選取回寫入儲存裝置(克隆目標) ")
    diskShow = enquiries.choose(' Choose clone disk options: ', options)
    diskGet = diskShow.split(' ')[1]

    osGet = ""
    osClone = subprocess.call(
            "sudo /usr/sbin/ocs-sr -g auto -e1 auto -e2 -r -j2 -k1 -scr -icds -p command restoredisk OS_TESTER/%s %s" %(osGet, diskGet), shell=True)
    if osClone != 0:
        print(Fore.RED + "FFFFFF______A______IIIIII____LL____" + Fore.RESET)
        print(Fore.RED + "FF_______AA___AA_____II______LL____" + Fore.RESET)
        print(Fore.RED + "FFFF_____AA___AA_____II______LL____" + Fore.RESET)
        print(Fore.RED + "FF_______AA___AA_____II______LL____" + Fore.RESET)
        print(Fore.RED + "FF_______AA_A_AA_____II______LL____" + Fore.RESET)
        print(Fore.RED + "FF_______AA___AA___IIIIII____LLLLLL" + Fore.RESET)
        print(" ")
        print("按任意鍵關機,n鍵返回主選單  ", end='')
        check = input("Press any key power off").lower()
        if check == ("n"):
            mMenu()
        os.system('systemctl poweroff')
    else:
        print(Fore.GREEN + "PPPPP_______A______SSSSSS___SSSSSS" + Fore.RESET)
        print(Fore.GREEN + "PP__PP____AA_AA____SS_______SS____" + Fore.RESET)
        print(Fore.GREEN + "PP___PP__AA___AA___SS_______SS____" + Fore.RESET)
        print(Fore.GREEN + "PP__PP___AA___AA___SSSSSS___SSSSSS" + Fore.RESET)
        print(Fore.GREEN + "PPPPP____AA___AA_______SS_______SS" + Fore.RESET)
        print(Fore.GREEN + "PP_______AA_A_AA_______SS_______SS" + Fore.RESET)
        print(Fore.GREEN + "PP_______AA___AA___SSSSSS___SSSSSS" + Fore.RESET)
        print(" ")
        print("按任意鍵關機,n鍵返回主選單  ", end='')
        check = input("Press any key power off").lower()
        if check == ("n"):
            mMenu()
        os.system('systemctl poweroff')

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
            time.sleep(3)
            break
        else:
            print(Fore.YELLOW + "外網測試失敗 Ping fail, check internet" + Fore.RESET)
            time.sleep(5)
    sys.stdout.flush()
    os.execv(sys.executable, ["python3"] + sys.argv)


mMenu()

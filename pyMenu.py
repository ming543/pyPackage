#!/bin/python3
import git
import os
import sys
import subprocess
import enquiries
import time
import re
from colorama import Fore
from colorama import Style

#start test file 
sT = "/home/production/data/ventoyTest/t.sh"
#Check system boot by UEFI or LEGACY mode
booted = "UEFI" if os.path.exists("/sys/firmware/efi") else "LEGACY"
#Get revision
#with open('revision', 'r') as r:
#    rev = r.read(5)
g = git.Git('.')
#loginfo = g.log('-p', '-1' , '--date=iso')
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')
#logData = loginfo.splitlines()
#rev = logData[2] + logData[4]

def mMenu():
    m1='Assy-Test (Label: SS02XXXX & CS04XXXX)'
    m2='PCBA-Test (Label: 000168-A0-SB000XXX)'
    m3='Other-Test'
    m4='BurnIn-Test'
    m5='OS Clone Setup'
    m6='OS Clone Execute'
    m7='Copy Log to Onedrive'
    m8='Update Linux Test Script'
    m9='Update DOS Test Script'
    ml='Power off system'
    options = [m1,m2,m3,m4,m5,m6,m7,m8,m9,ml]

    os.system('clear')
    print(Fore.YELLOW + "%s MAIN-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, options)

    if choice == m1: #Assy test
        aMenu()
    elif choice == m2: #PCBA test
        pMenu()
    elif choice == m3: #other test
        oMenu()
    elif choice == m4: #Burnin test
        bMenu()
    elif choice == m5: #OS clone setup
        osSetup()
    elif choice == m6: #OS clone Execute
        osExec()
    elif choice == m7: #copy log to onedrive
        copyLog()
    elif choice == m8: #Update Linux script
        gitPull()        
    elif choice == m9: #Update DOS script
        dosMenu()
    #Last of list
    elif choice == ml: #power off system
        print("The system will shutdown after 5 secs!")
        time.sleep(5)
        os.system('systemctl poweroff')

# 2 steps pn pick, aMenu+aaMenu
def aaaMenu():
    a1='10953-0000'
    a2='20010-0000'
    al='Back to MAIN-MENU'
    options = [a1,a2,al]
    os.system('clear')
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, options)
    if choice == a1:
        aaMenu(a1)
    elif choice == a2:
        aaMenu(a2)
    elif choice == al:
        print(choice)
        mMenu()
def aaMenu(aOptions):
    index = []
    aPath = "/home/production/data/ventoyTest/testAssy"
    os.system('clear')
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    #Check only match PN list of aaMenu
    for filename in os.listdir(aPath):
        if re.match(aOptions, filename):
            index += [filename]
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, index)
    for i in range(len(index)):
        if choice == index[i]:
            f = open(sT, "w") #sT is start test t.sh file
            f.write("cd /home/production/data/ventoyTest/testAssy && python3 %s" % index[i])
            f.close()
            print(index[i])
            subprocess.call("sh %s" % sT , shell=True)

#Show all PN of testAssy
def aMenu():
    index = []
    aPath = "/home/production/data/ventoyTest/testAssy"
    os.system('clear')
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    for filename in os.listdir(aPath):
        index += [filename]
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, index)
    for i in range(len(index)):
        if choice == index[i]:
            f = open(sT, "w") #sT is start test t.sh file
            f.write("cd /home/production/data/ventoyTest/testAssy && python3 %s" % index[i])
            f.close()
            print(index[i])
            subprocess.call("sh %s" % sT , shell=True)

def pMenu():
    p1='p1'
    p2='p2'
    pl='Back to MAIN-MENU'
    options = [p1,p2,pl]
    os.system('clear')
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, options)
    if choice == p1:
        print("p1 is")
    elif choice == p2:
        print("p2 is")
    elif choice == pl:
        mMenu()

def oMenu():
    o1='o1'
    o2='o2'
    ol='Back to MAIN-MENU'
    options = [o1,o2,ol]
    os.system('clear')
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Style.RESET_ALL + " Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    choice = enquiries.choose(Fore.YELLOW + '  Choose one of these options: ' + Style.RESET_ALL, options)
    if choice == o1:
        print("o1 is")
    elif choice == o2:
        print("o2 is")
    elif choice == ol:
        mMenu()

def bMenu():
    print("BI tool here")
    time.sleep(5)
    mMenu()

def osSetup():
    print("OS setup tool here")
    time.sleep(5)
    mMenu()

def osExec():
    print("OS Exec tool here")
    time.sleep(5)
    mMenu()

def copyLog():
    #os.system('clear')
    for i in range(5): #ping 5 times
        response = os.system("ping -c 1 -w 1 8.8.8.8")
        if response == 0:
            print("PING OK")
            localFolder = "/home/production/data/log"
            onedriveFolder = "ID-Enbik:General/log"
            retcode = subprocess.call("rclone -v copy %s %s -P" %(localFolder, onedriveFolder), shell=True)
            if retcode == 0: #check rclone pass or fail
                print(Fore.GREEN + "Log copy to onedrive done!!!" + Style.RESET_ALL)
                time.sleep(5)
                break
            else:
                print(Fore.RED + "Log copy to onedrive Fail!!!" + Style.RESET_ALL)
                time.sleep(5)
                break
        else:
            print(Fore.YELLOW + "PING 8.8.8.8 Fail, Please check internet cable" + Style.RESET_ALL)
            time.sleep(1)
    mMenu()

def gitPull():
    #os.system('clear')
    for i in range(5): #ping 5 times
        response = os.system("ping -c 1 -w 1 8.8.8.8")
        if response == 0:
            print("PING OK")
            #os.chdir('/home/production/data/ventoyTest')
            g.gc()
            g.fetch('--all')
            g.reset('--hard')
            g.clean('-f', '-d')
            g.pull()
            print("gitPullDone")
            time.sleep(1)
            break 
        else:
            print(Fore.YELLOW + "PING 8.8.8.8 Fail, Please check internet cable" + Style.RESET_ALL)
            time.sleep(5)

    sys.stdout.flush()
    os.execv(sys.executable, ["python3"] + sys.argv)

def dosMenu():
    print("dos tool here")
    time.sleep(5)
    mMenu()

mMenu()


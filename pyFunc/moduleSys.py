#!/bin/python3
import git
import os
# import sys
import logging
import shelve
import getmac
import time
# import datetime
import re
import subprocess
import enquiries
import cpuinfo
from colorama import Fore

# logging.basicConfig(level=logging.DEBUG)
# log_filename = datetime.datetime.now().strftime(sn + "-%Y-%m-%d-%H:%M:%S.log")
# logging.basicConfig(level=logging.INFO)

# Check system boot by UEFI or LEGACY mode
booted = "UEFI" if os.path.exists("/sys/firmware/efi") else "LEGACY"

# Get revision
g = git.Git('.')
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')


#sT = "/home/production/pyPackage/t.sh"
startTest = "/home/stux/pyPackage/t.sh"
logPath = "/media/sda2/log/"
if os.path.isdir(logPath):
    print(" ")
else:
    subprocess.check_call("sudo mount /dev/sda2 /media/sda2 -o umask=000", shell=True, stdin=sys.stdin)


def pnGet():
    print(Fore.YELLOW + " Choose PN number for Test and Log! " + Fore.RESET)
    index = ['10300-', '10400-', '10500-', '10901-', '10902-', '10951-', '10953-', '20010-']
    indexChoice = enquiries.choose('  Choose options: ', index)
    body = []
    for i in range(1, 10):
        #add number by six digi, someday may used.
        #body.append(indexChoice + "{:06d}".format(i))
        body.append(indexChoice + '000' + str(i))
    bodyFirst = enquiries.choose(' Choose body: ', body)
    body.clear()
    for j in range(1, 10):
        body.append(bodyFirst + str(j))
    bodySecond = enquiries.choose(' Choose body: ', body)
    body.clear()
    for k in range(1, 10):
        body.append(bodySecond + str(k))
    bodyThird = enquiries.choose(' Choose body: ', body)
    body.clear()
    rev = [bodyThird + '-A.', bodyThird + '-B.', bodyThird + '-C.', bodyThird + '-D.', bodyThird + '-E.']
    revChoice = enquiries.choose('  Choose Revision: ', rev)
    for p in range(1, 10):
        body.append(revChoice + str(p))
    pn = enquiries.choose('  Choose PN: ', body)
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['pnSave'] = pn

def pnGet2():
    index = []
    aPath = "/home/stux/pyPackage/testAssy"
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    for filename in os.listdir(aPath):
        index += [filename]
    choice = enquiries.choose('  Choose options: ', index)
    for i in range(len(index)):
        if choice == index[i]:
            return index[i]


def pnCheck():
    os.system('clear')
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        pn = db['pnSave'] 
    print(Fore.YELLOW + " Check PN number for Test and Log! " + Fore.RESET)
    print("Test_PN: " + pn)
    pnCheck = input("Back to menu press 'n', other key continue: ").lower()
    if pnCheck == "n":
        return False
    else:
        return True


# pn input form script
def snGet(pn, modelName):
    os.system('clear')
    print("Test_Model: " + modelName)
    print("Test_PN: " + pn)
    print("Back to menu press 'n', Input SN start test: ")
    global sn
    sn = input()
    sn = str(sn)
    #with shelve.open('snTemp') as db:
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['snSave'] = sn

    if sn == "n":
        print("Start Test is " + startTest)
        with open(startTest, "w") as f:
            f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
        subprocess.call("sh %s" % startTest, shell=True)
    else:
        # setup test start time
        startTime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        # setup test log month folder
        logMonth = time.strftime("%Y%m", time.localtime())
        logFilename = sn + "-" + modelName + "-" + startTime + ".log"
        global log
        log = logPath + pn + "/" + logMonth + "/" + logFilename
        os.makedirs(os.path.dirname(log), exist_ok=True)  # Create log folder
        # save log name and location to database
        # with shelve.open('snTemp') as db:
        with shelve.open('/home/stux/pyPackage/dataBase') as db:
            db['log'] = log

        logger = logging.getLogger()
        # Setup logging level
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                datefmt='%Y%m%d %H:%M:%S')

        # Setup log show on stream and file both
        ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        # log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        # fh = logging.FileHandler(log_filename)
        fh = logging.FileHandler(log)
        # fh.setLevel(logging.DEBUG)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)
        logging.info('Test_Model: ' + modelName)
        logging.info('Test_PN: ' + pn)
        logging.info('Test_SN: ' + sn)
        # logging.debug('debug')
        # logging.info('info')
        # logging.warning('warning')
        # logging.error('error')
        # logging.critical('critical')

#dmiFunc ex.baseboard-product-name
def biFuncCheck():
    biosN = subprocess.check_output("sudo dmidecode -s baseboard-product-name", shell=True)
    biosN = str(biosN)
    if re.search("V([0-9]C)", biosN):
        return True
    else:
        return False

def dmidecodeCheck(dmiFunc, spec):
    biosN = subprocess.check_output("sudo dmidecode -s %s" % dmiFunc, shell=True)
    biosN = str(biosN)
    if re.search(spec, biosN):
        logging.info(dmiFunc + ': ' + biosN + " SPEC: " + spec)
        return True
    else:
        logging.error(dmiFunc + ': ' + biosN + " SPEC: " + spec)
        failRed()		


def biosVersionCheck(spec):
    biosV = subprocess.check_output("sudo dmidecode -s bios-version", shell=True)
    biosV = str(biosV)
    if re.search(spec, biosV):
        logging.info('BIOS_Version: ' + biosV + " SPEC: " + spec)
    else:
        logging.error('BIOS_Version: ' + biosV + " SPEC: " + spec)
        failRed()

		
def rtcCheck():
    y = "2021"  # check years of BIOS time
    rtcTime = subprocess.check_output("sudo hwclock -r", shell=True)
    rtcTime = str(rtcTime)
    if re.search(y, rtcTime):
        logging.info('RTC_Time: ' + rtcTime + " SPEC: " + y)
    else:
        logging.error('RTC_Time: ' + rtcTime + " SPEC: " + y)
        failRed()


def macCheck(macA, macH):
    ethMac = getmac.get_mac_address(interface=macA)
    if re.search(macH, ethMac):
        logging.info('Test_MAC: ' + macA + "_" + ethMac + " SPEC: " + macH)
    else:
        logging.error('Test_MAC: ' + macA + "_" + ethMac + " SPEC: " + macH)
        failRed()


def failRed():
    logging.error('****** TEST_FAILED! ******')
    logFail = log + ".FAIL"
    os.replace(log, logFail)
    print(Fore.RED + "Fail" + Fore.RESET)
    check = input("Press 'n' power off, other key re-test: ").lower()
    if check == ("n"):
        os.system('systemctl poweroff')
    subprocess.call("sh %s" % startTest, shell=True)


def cpuInfo():
    c = cpuinfo.get_cpu_info()['brand_raw']
    logging.info('CPU_Info: ' + c)
    print(Fore.YELLOW + "Check CPU with BOM" + Fore.RESET)
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('CPU_Info: ' + c + ' not match BOM')
        failRed()


def getCpuMips():
    with open('/proc/cpuinfo', 'r') as infos:
        for line in infos:
            if line.lower().startswith('bogomips'):
                mips = line.split(':')[1].lstrip().split('\n')[0]
        return mips

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
sT = "/home/stux/pyPackage/t.sh"
logPath = "/media/sda2/log/"
if os.path.isdir(logPath):
    print(" ")
else:
    subprocess.check_call("sudo mount /dev/sda2 /media/sda2 -o umask=000", shell=True, stdin=sys.stdin)

	

def pnGet():
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


# pn input form script
def snGet(pn, modelName):
    os.system('clear')
    print("Test_Model: " + modelName)
    print("Test_PN: " + pn)
    print("Back to menu press 'n', Input SN start test: ")
    global sn
    sn = input()
    sn = str(sn)
    with shelve.open('snTemp') as db:
        db['snSave'] = sn

    if sn == "n":
        print("Start Test is " + sT)
        with open(sT, "w") as f:
            f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
        subprocess.call("sh %s" % sT, shell=True)
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
        with shelve.open('snTemp') as db:
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


def biosBaseNameCheck(spec):
    biosN = subprocess.check_output("sudo dmidecode -s baseboard-product-name", shell=True)
	if re.search(spec, biosN):
		logging.info('Baseboard_Name: ' + biosN + " SPEC_" + spec)
    else:
        logging.error('Baseboard_Name: ' + biosN + " SPEC_" + spec)
        failRed()		

		
def biosVersionCheck(spec):
    biosV = subprocess.check_output("sudo dmidecode -s bios-version", shell=True)
	if re.search(spec, biosV):
		logging.info('BIOS_Version: ' + biosV + " SPEC_" + spec)
    else:
        logging.error('BIOS_Version: ' + biosV + " SPEC_" + spec)
        failRed()

		
def rtcCheck():
    y = "2021"  # check years of BIOS time
    rtcTime = subprocess.check_output("sudo hwclock -r", shell=True)
    rtcTime = str(rtcTime)
    if re.search(y, rtcTime):
        logging.info('RTC_Time: ' + rtcTime + " SPEC_" + y)
    else:
        logging.error('RTC_Time: ' + rtcTime + " SPEC_" + y)
        failRed()


def macCheck(macA, macH):
    ethMac = getmac.get_mac_address(interface=macA)
    if re.search(macH, ethMac):
        logging.info('Test_MAC: ' + macA + "_" + ethMac + " SPEC_" + macH)
    else:
        logging.error('Test_MAC: ' + macA + "_" + ethMac + " SPEC_" + macH)
        failRed()


def failRed():
    logging.error('****** TEST_FAILED! ******')
    logFail = log + ".FAIL"
    os.replace(log, logFail)
    print(Fore.RED + "Fail" + Fore.RESET)
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        os.system('systemctl poweroff')
    subprocess.call("sh %s" % sT, shell=True)


def cpuInfo():
    c = cpuinfo.get_cpu_info()['brand_raw']
    logging.info('CPU_Info: ' + c)
    print(Fore.YELLOW + "Check CPU with BOM" + Fore.RESET)
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('CPU_Info: ' + c + ' not match BOM')
        failRed()




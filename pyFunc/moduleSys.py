#!/bin/python3
import os
# import sys
import logging
import shelve
import getmac
import time
# import datetime
import re
import subprocess

# logging.basicConfig(level=logging.DEBUG)
# log_filename = datetime.datetime.now().strftime(sn + "-%Y-%m-%d-%H:%M:%S.log")
# logging.basicConfig(level=logging.INFO)

sT = "/home/production/pyPackage/t.sh"

loc = "/home/production"
# loc = "/media/production/data"
logPath = loc + "/log/"
print(logPath)
# pn = "10953-000001-B.0/" # pn for U6-500


def snGet(pn):
    os.system('clear')
    print("Input 0000 back to Main, Input SN start test: ")
    global sn
    sn = input()
    sn = str(sn)
    with shelve.open('snTemp') as db:
        db['snSave'] = sn

    if sn == "0000":
        print("sT is " + sT)
        f = open(sT, "w")  # sT is start test t.sh file
        f.write("cd /home/production/pyPackage && python3 pyMenu.py")
        f.close()
        subprocess.call("sh %s" % sT, shell=True)
    else:
        # setup test start time
        startTime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        # setup test log month folder
        logMonth = time.strftime("%Y%m", time.localtime())
        logFilename = sn + "-" + startTime + ".log"
        global log
        log = logPath + pn + "/" + logMonth + "/" + logFilename
        os.makedirs(os.path.dirname(log), exist_ok=True)  # Create log folder
        with shelve.open('snTemp') as db:
            db['log'] = log

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                datefmt='%Y%m%d %H:%M:%S')

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
        logging.info('Test PN : ' + pn)
        logging.info('Test SN : ' + sn)
        # log = open(logLoc, "w")
        # log.writelines ("Test start time: " + startTime + "\n")
        # log.writelines ("Test SN: " + sn + "\n")
        # log.writelines (" " + "\n")
        # logging.debug('debug')
        # logging.info('info')
        # logging.warning('warning')
        # logging.error('error')
        # logging.critical('critical')


def rtcCheck():
    y = "2021"  # check years of BIOS time
    rtcTime = subprocess.check_output("sudo hwclock -r", shell=True)
    rtcTime = str(rtcTime)
    if re.search(y, rtcTime):
        logging.info('RTC Time : ' + rtcTime + " SPEC is " + y)
    else:
        logging.error('Fail RTC Time : ' + rtcTime + " SPEC is " + y)


def macCheck(macA, macH):
    ethMac = getmac.get_mac_address(interface=macA)
    if re.search(macH, ethMac):
        logging.info('Test MAC : ' + macA + " " + ethMac + " SPEC is " + macH)
    else:
        logging.error('Fail Test MAC : ' + macA + " " + ethMac + " SPEC is " + macH)
        failRed()


def failRed():
    logging.error('****** TEST_FAILED! ******')
    logFail = log + ".FAIL"
    os.replace(log, logFail)
    print("Fail, Press any key test again")
    input()
    subprocess.call("sh %s" % sT, shell=True)
    # quit()

# with shelve.open('snTemp') as db:
#    sn = db['snSave']
# print(sn)

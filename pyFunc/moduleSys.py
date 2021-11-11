#!/bin/python3
import os
import sys
import logging
import shelve
import getmac
import time
import datetime
import re
import subprocess



#logging.basicConfig(level=logging.DEBUG)
#log_filename = datetime.datetime.now().strftime(sn + "-%Y-%m-%d-%H:%M:%S.log")
#logging.basicConfig(level=logging.INFO)




loc="/home/production"
#loc="/media/production/data"
logPath = loc + "/log/"
print(logPath)
pn = "10953-000001-B.0/" #pn for U6-500



def snGet():
    os.system('clear')
    print("Test Start, input SN")
    global sn 
    sn = input()
    with shelve.open('snTemp') as db:
        db['snSave'] = sn

    startTime = time.strftime("%Y%m%d-%H%M%S",time.localtime()) #setup test start time
    logMonth = time.strftime("%Y%m",time.localtime()) #setup test log month folder
    logFilename = sn + "-" + startTime + ".log"
    global log 
    log = logPath + pn + logMonth + "/" + logFilename
    os.makedirs(os.path.dirname(log), exist_ok=True) # Create log folder 
    with shelve.open('snTemp') as db:
        db['log'] = log

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
	    '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
	    datefmt='%Y%m%d %H:%M:%S')

    ch = logging.StreamHandler()
    #ch.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
 
    #log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
    #fh = logging.FileHandler(log_filename)
    fh = logging.FileHandler(log)
    #fh.setLevel(logging.DEBUG)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    logging.info('Test PN : ' + pn)
    logging.info('Test SN : ' + sn)
    
    #log = open(logLoc, "w")
    #log.writelines ("Test start time: " + startTime + "\n")
    #log.writelines ("Test SN: " + sn + "\n")
    #log.writelines (" " + "\n")
    #logging.debug('debug')
	#logging.info('info')
	#logging.warning('warning')
	#logging.error('error')
	#logging.critical('critical')
    




def rtcCheck():
    y="2021" #check years of BIOS time
    rtcTime = subprocess.check_output("sudo hwclock -r", shell=True)
    rtcTime = str(rtcTime)
    if re.search(y, rtcTime):
        logging.info('RTC Time : ' + rtcTime + " SPEC is " + y)
    else:
        logging.error('Fail RTC Time : ' + rtcTime + " SPEC is " + y)

def macCheck(macA, macH):
    ethMac = getmac.get_mac_address(interface = macA)
    if re.search(macH, ethMac):
        logging.info('Test MAC : ' + macA + " is " + ethMac + " SPEC is " + macH)
    else:
        logging.error('Fail Test MAC : ' + macA + " is " + ethMac + " SPEC is " + macH)
        failRed()

def failRed():
    logging.error('****** TEST_FAILED! ******')
    logFail = log + ".FAIL"
    os.replace(log,logFail)
    print("Fail")
    input()
    quit()
   

snGet()
macCheck("enp4s0","00:13:95")
rtcCheck()
failRed()

with shelve.open('snTemp') as db:
    sn = db['snSave']
#print(sn)


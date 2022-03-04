#!/bin/python3
import git
import os
import sys
import logging
import shelve
import getmac
import time
# import datetime
import re
import subprocess
import enquiries
import cpuinfo
import netifaces
import serial
import pexpect
from colorama import Fore
from pyFunc.moduleSys import failRed

pyFolder = "/home/stux/pyPackage/"
ekitFolder = pyFolder + "tools/EKit_L"

def aicVersion(aicSpec):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('( 1)*') #System Info
    process.sendline("1\r")
    process.expect("( 1)*") #Firmware Info
    process.sendline("1\r")
    process.expect("(Exit)*") #Firmware Info
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(r'AIC', result[i]):
            j = result[i]
    if re.search(aicSpec, j):
        logging.info('AIC_Revision:%s SPEC:%s' %(j, aicSpec))
    else:
        logging.error('AIC_Revision_Fail:%s SPEC:%s' %(j, aicSpec))
        failRed('AIC_Revision_Fail:%s SPEC:%s' %(j, aicSpec))


def aicDdmLogo():
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('( 2)*') #DDM Info
    process.sendline("2\r")
    process.expect("( 3)*") #DDM Page Config Info
    process.sendline("3\r")
    process.expect("(Exit)*") #Firmware Info
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(r'Logo', result[i]):
            j = result[i]
    if re.search('None', j):
        logging.info('AIC_DDM_Logo:%s SPEC: None' % j)
    else:
        logging.error('AIC_DDM_Logo:%s SPEC: None' % j)
        failRed('AIC_DDM_Logo:%s SPEC: None' % j)

def aicTemp(tempL, tempH):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('( 3)*') #Health Monitoring
    process.sendline("3\r")
    process.expect("( 1)*") #System Health
    process.sendline("1\r")
    process.expect("(Exit)*") #Temp Info
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(r'Temperature', result[i]):
            sysTemp = result[i].split()[1]
            sysTemp = int(sysTemp)
    if tempL < sysTemp < tempH:
        logging.info('AIC_Temp: %sC SPEC:%s - %s' % (sysTemp, tempL, tempH))
    else:
        logging.error('AIC_Temp_Fail: %sC SPEC: %s -%s' % (sysTemp, tempL, tempH))
        failRed('AIC_Temp_Fail: %sC SPEC: %s - %s' %(sysTemp, tempL, tempH))

def aicRtc(L, H):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('( 3)*') #Health Monitoring
    process.sendline("3\r")
    process.expect("( 4)*") #Hardware Monitor
    process.sendline("4\r")
    process.expect("(Exit)*") #Temp Info
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(r'RTC', result[i]):
            sysRtc = result[i].split()[4]
            sysRtc = float(sysRtc)
            print(sysRtc)
    if L < sysRtc < H:
        logging.info('AIC_RTC: %sV SPEC:%s - %s' % (sysRtc, L, H))
    else:
        logging.error('AIC_RTC_Fail: %sV SPEC: %s -%s' % (sysRtc, L, H))
        failRed('AIC_RTC_Fail: %sV SPEC: %s - %s' %(sysRtc, L, H))

def aicPoe(port):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('( 4)*') #PoE
    process.sendline("4\r")
    process.expect("( 3)*") #Poe Status
    process.sendline("3\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(port, result[i]):
            #print(result[i])
            j = result[i]
            poeCheck = result[i].split()[3]
            poeCheck = str(poeCheck)
            #print(poeCheck)
    if poeCheck != "Disconnected" :
        logging.info('AIC_PoE: %s' % j)
    else:
        logging.error('AIC_PoE_Fail: %s' % j)
        failRed('AIC_PoE_Fail: %s' % j)


def aicFan(port):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(10)*') #Fan
    process.sendline("10\r")
    process.expect("( 3)*") #Fan Status
    process.sendline("3\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(port, result[i]):
            #print(result[i])
            j = result[i]
            fanCheck = result[i].split()[3]
            fanCheck = int(fanCheck)
            #fanCheck = str(fanCheck)
            print(fanCheck)
    if fanCheck != 0 :
        logging.info('AIC_Fan: %s' % j)
    else:
        logging.error('AIC_Fan_Fail: %s' % j)
        failRed('AIC_Fan_Fail: %s' % j)


def aicIdio(port, data):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(11)*') #IO
    process.sendline("11\r")
    process.expect("( 1)*") #IDIO Pins Status
    process.sendline("1\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(port, result[i]):
            #print(result[i])
            j = result[i]
            portCheck = result[i].split()[0]
            dataCheck = result[i].split()[1]
            dataCheck = int(dataCheck)
            #print(fanCheck)
    if portCheck == port:
        logging.info('AIC_IDIO: %s SPEC: %s' % (j, port))
    else:
        logging.error('AIC_IDIO_Fail: %s SPEC: %s' % (j, port))
        failRed('AIC_IDIO_Fail: %s SPEC: %s' % (j, port))
    if dataCheck != data:
        logging.error('AIC_IDIO_Data_Fail: %s SPEC: %s' % (j, port))
        failRed('AIC_IDIO_Fail: %s SPEC: %s' % (j, port))
## Not check DIO data for now
#    else:
#        logging.info('AIC_IDIO_Data:%s SPEC:%s' % (j, data))


def aicDio(port, data):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(11)*') #IO
    process.sendline("11\r")
    process.expect("( 6)*") #DIO Pins Status
    process.sendline("6\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(len(result)):
        if re.search(port, result[i]):
            #print(result[i])
            j = result[i]
            portCheck = result[i].split()[0]
            dataCheck = result[i].split()[1]
            dataCheck = int(dataCheck)
            #print(fanCheck)
    if portCheck == port:
        logging.info('AIC_DIO: %s SPEC: %s' % (j, port))
    else:
        logging.error('AIC_DIO_Fail: %s SPEC: %s' % (j, port))
        failRed('AIC_DIO_Fail: %s SPEC: %s' % (j, port))
    if dataCheck != data:
        logging.error('AIC_DIO_Data_Fail: %s SPEC: %s' % (j, port))
        failRed('AIC_DIO_Fail: %s SPEC: %s' % (j, port))
#    else:
#        logging.info('AIC_IDIO_Data:%s SPEC:%s' % (j, data))

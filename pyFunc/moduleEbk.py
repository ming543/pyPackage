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
from colorama import Fore, Back, Style
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
    for i in range(1, port + 1):
        poeCheck = False
        for j in range(len(result)):
            if re.search(r"PoE  %s Present:" % i, result[j]):
                poeCheck = True
                poeLog = result[j]
                poePower = result[j].split()[3]
                logging.info(result[j])
        if poePower == "Disconnected":
            logging.error('PoE %s Fail: ' % i + poeLog)
            failRed('PoE %s Fail: ' % i + poeLog)
                
        if poeCheck != True:
            logging.error('PoE  %s Present: Fail' % i + poeLog)
            failRed('PoE  %s Present: Disconnected' % i + poeLog)
            

def opPoe(port):
    if port != 0:
        os.system('clear')
        print(" ")
        print(Fore.BLUE + Back.WHITE)
        print("PoE測具燈號確認 PoE Tester LED Check")
        print(Fore.MAGENTA + Back.WHITE)
        print("確認PoE燈號是否顯示 Check PoE tester LED is light")
        print(Style.RESET_ALL)
        print("不良按n鍵結束,其他鍵繼續  ", end='')
        check = input("Failed press 'n', other key continue: ").lower()
        if check == ("n"):
            logging.error('PoE_LED_Check: Fail ')
            failRed("PoE LED 燈號不良")
        logging.info('PoE_LED_ON: Display OK')

                

def aicFan(port):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(10)*') #Fan
    process.sendline("10\r")
    process.expect("( 2)*") #Fan Config
    process.sendline("2\r")
    process.expect("Select one, and config.") #Fan Config
    process.sendline("2,0,80\r")
    time.sleep(1)
    process.expect("(Quit)*") 
    process.sendline("q\r")
    process.expect("( 3)*") #Fan Status
    process.sendline("3\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    for i in range(1, port + 1):
        fanCheck = False
        for j in range(len(result)):
            if re.search(r' Fan %s RPM:' %i, result[j]):
                fanCheck = True
                fanLog = result[j]
                fanRpm = result[j].split()[3]
                fanRpm = int(fanRpm)
                logging.info(fanLog)
        if fanRpm == 0:
            logging.error('Fan %s RPM Fail:' %i + fanLog)
            failRed(' Fan %s RPM Fail: ' %i + fanLog)
        if fanCheck != True:
            logging.error('Fan %s not find!' %i)
            failRed(' Fan %s not find!' %i)
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(10)*') #Fan
    process.sendline("10\r")
    process.expect("( 2)*") #Fan Config
    process.sendline("2\r")
    process.expect("Select one, and config.") #Fan Config
    process.sendline("2,1\r")
    process.expect("(Quit)*") 
    process.sendline("q\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
        
        
def aicDioSelect(sDio):
    if sDio == "1D2D":
        aicDio("GPIO1")
        aicDio("GPIO2")
    elif sDio == "1I2D":
        #1I
        print(Fore.BLUE + Back.WHITE)
        print("Test IDIO-ONE")
        print(Style.RESET_ALL)
        aicIdioConfig("DIO1", "SOURCE")
        aicIdioCheck("DIO1")
        aicIdioConfig("DIO1", "SINK")
        aicIdioCheck("DIO1")
        #2D
        aicDio("GPIO2")
    elif sDio == "1I2I":
        #1I
        print(Fore.BLUE + Back.WHITE)
        print("Test IDIO-ONE")
        print(Style.RESET_ALL)
        aicIdioConfig("DIO1", "SOURCE")
        aicIdioCheck("DIO1")
        aicIdioConfig("DIO1", "SINK")
        aicIdioCheck("DIO1")
        #2I
        print(Fore.BLUE + Back.WHITE)
        print("Test IDIO-TWO")
        print(Style.RESET_ALL)
        aicIdioConfig("DIO2", "SOURCE")
        aicIdioCheck("DIO2")
        aicIdioConfig("DIO2", "SINK")
        aicIdioCheck("DIO2")
    elif sDio == "1I":
        aicIdioConfig("DIO1", "SOURCE")
        aicIdioCheck("DIO1")
        aicIdioConfig("DIO1", "SINK")
        aicIdioCheck("DIO1")
    elif sDio == "1D":
        aicDio("GPIO1")

#mode(0:SINK-II, 1:SOURCE-I)
def aicIdioConfig(port, mode):
    print(Fore.MAGENTA + Back.WHITE)
    if mode =="SINK":
        print("Set IDIO Switch to - II")
    elif mode =="SOURCE":
        print("Set IDIO Switch to - I")
    print(Style.RESET_ALL)
    input("按任意鍵繼續 Press any key continue...")

    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(11)*') #IO
    process.sendline("11\r")
    process.expect("( 3)*") #IDIO Pins Config
    process.sendline("3\r")
    process.expect("DOTYPE")
    if port == "DIO1" and mode =="SINK":
        process.sendline("1, 0\r" )
    elif port == "DIO1" and mode =="SOURCE":
        process.sendline("1, 1\r" )
    elif port == "DIO2" and mode =="SINK":
        process.sendline("2, 0\r" )
    elif port == "DIO2" and mode =="SOURCE":
        process.sendline("2, 1\r" )
    process.expect("(Q)*") 
    process.sendline("q\r")
    process.expect("( 5)*") 
    process.sendline("5\r")
    process.expect("GROUP_DATA")
    if port == "DIO1":
        process.sendline("1, FF\r" )
    if port == "DIO2":
        process.sendline("2, FF\r" )
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    portCheck = ""
    dataCheck = ""
    for i in range(len(result)):
        if re.search("C   C", result[i]):
            j = result[i]
            portCheck = result[i].split()[0]
            dataCheck = result[i].split()[1]
    if portCheck == port and dataCheck == "FF":
        logging.info('AIC_IDIO_CONFIG: %s %s SPEC: %s %s' % (portCheck, dataCheck, port, mode))
        #print("j: ", j)
    else:
        logging.error('IDIO_PORT_CONFIG_CHECK_Fail: %s SPEC: %s %s' % (j, port, mode))
        failRed('IDIO_PORT_CONFIG: Failed! SPEC: %s %s' % (port, mode))


def aicIdioCheck(port):
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
    portCheck = ""
    dataCheck = ""
    for i in range(len(result)):
        if re.search("C   C|NC  NC", result[i]):
            j = result[i]
        else:
            logging.error('IDIO_PORT_CHECK_Fail: %s SPEC:( 4)DO' % result[-6])
            failRed('IDIO_PORT_CHECK: Failed! %s SPEC:( 4)DO' % result[-6])
        if re.search(port, result[i]):
            portCheck = result[i].split()[0]
            dataCheck = result[i].split()[1]

    if portCheck == port and dataCheck == "FF":
        logging.info('AIC_IDIO_CHECK: %s %s SPEC: %s FF' % (portCheck, dataCheck, port))
        #print("j: ", j)
    else:
        logging.error('IDIO_PORT_CHECK_Fail: %s SPEC: %s FF' % (j, port))
        failRed('IDIO_PORT_CHECK: Failed! SPEC: %s FF' % (port))


def aicDio(port):
    process = pexpect.spawn('make run', cwd=ekitFolder, timeout=2, encoding='utf-8' )
    process.expect('(11)*') #IO
    process.sendline("11\r")
    process.expect("( 9)*") #DIO Pins Status
    process.sendline("9\r")
    process.expect("(Exit)*") 
    process.sendline("exit\r")
    process.expect(pexpect.EOF)
    result = process.before
    result = str(result).splitlines()
    portCheck = ""
    dataCheck = ""
    #print(result)
    for i in range(len(result)):
        if re.search('Low   Low', result[i]):
            j = result[i]
    #    else:
    #        logging.error('DIO_PORT_CHECK_Fail: %s SPEC:( 9)GPIO' % result[-6])
    #        failRed('DIO_PORT_CHECK: Failed! %s SPEC:( 9)GPIO' % result[-6])
        if re.search(port, result[i]):
            portCheck = result[i].split()[0]
            dataCheck = result[i].split()[1]
       # try:
       #     dataCheck = int(dataCheck)
       # except:
       #     logging.error('AIC_DIO_Data_Fail: %s SPEC: %s %s' % (portCheck, port, data))
       #     failRed('AIC_DIO_Fail: %s SPEC: %s %s' % (portCheck, port, data))
    if portCheck == port and dataCheck == "0000":
        logging.info('AIC_DIO_PORT: %s %s SPEC: %s 0000' % (portCheck, dataCheck, port))
    else:
        logging.error('DIO_PORT_CHECK_Fail: %s SPEC: %s 0000' % (j, port))
        failRed('DIO_PORT_CHECK: Failed! SPEC: %s 0000' % port)

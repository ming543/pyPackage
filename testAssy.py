#!/bin/python3
import os
import shelve
import inspect
import subprocess
from colorama import Fore, Back, Style
from pyFunc import moduleSys
from pyFunc import moduleEbk
#from pyFunc import moduleCg
import testBi
import osClone

startTest = "/home/stux/pyPackage/t.sh"
#Get PN from db
with shelve.open('/home/stux/pyPackage/dataBase') as db:
    pn = db['pnSave']

def AIM(sCPU, sPoe, sFan, sDio, sLan, sCom, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2019")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    moduleEbk.opPoe(sPoe)
#    moduleEbk.aicPoe(sPoe)
#    moduleEbk.aicFan(sFan)
    moduleEbk.aicDioSelect(sDio)
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanSpeedSet(sLan, 100)
    moduleSys.lanLedCheckAll()
    moduleSys.lanSelect(sLan)
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleSys.uartLoopCheck(sCom)
    moduleSys.alsabatTest()
#    moduleSys.cpuTempCheck(20, 60)


def AIH(sCPU, sPoe, sFan, sDio, sLan, sCom, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    moduleSys.biosReleaseCheck("11/11/2020")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
    #moduleEbk.aicPoe(sPoe)
    moduleEbk.opPoe(sPoe)
    moduleEbk.aicFan(sFan)
    moduleEbk.aicDioSelect(sDio)
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanSpeedSet(sLan, 100)
    moduleSys.lanLedCheckAll()
    moduleSys.lanSelect(sLan)
    moduleSys.uartLoopCheck(sCom)
    moduleSys.alsabatTest()
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 3)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
#    moduleSys.cpuTempCheck(20, 60)


def CJB(sCPU, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("Mouse", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleCg.i2cGpio()
    moduleSys.uartLoop("/dev/ttyS0")
    moduleSys.aplayTest()
    moduleSys.arecordTest()
    #moduleSys.cpuTempCheck(20, 60)


def Q715QA5OS(sBat):
    moduleSys.ntpTime(sBat)
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.atCheck("/dev/ttyUSB2", "at+qccid", "CCID")
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck(sBat)
    moduleSys.cpuCheck("E3930")
    moduleSys.memoryCheckOne("2048")
    moduleSys.storageCheck("mmcblk1")
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.lanSpeedSet(2, 100)
    moduleSys.lanLedCheck(" 綠Green - 橘Orange ")
    moduleSys.lanLedOffCheck(" 滅Off - 滅Off")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("JMS567", 1)
    #SIM7600
#    moduleSys.atCheck("/dev/ttyUSB2", "ati", "Rev")
#    moduleSys.atCheck("/dev/ttyUSB2", "ati", "IMEI")
#    moduleSys.atCheck("/dev/ttyUSB2", "at+cgmr", "CGMR")
#    moduleSys.atCheck("/dev/ttyUSB2", "at+ciccid", "ICCID")
    #EC25
    #test AT command time can't too close
    moduleSys.atCheck("/dev/ttyUSB2", "ati/r/n", "Rev")
    moduleSys.cpuTempCheck(20, 55)
    osClone.osCloneFix("2022-02-07-09-img-Q715QA5-EMMC-32G", "mmcblk1")


def U7130PAS(sCPU, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("Mouse", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleSys.uartLoop("/dev/ttyS0")
    #moduleSys.cpuTempCheck(20, 60)


def U7130(sCPU, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("Mouse", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleCg.i2cGpio()
    moduleSys.uartLoop("/dev/ttyS0")
    moduleSys.aplayTest()
    moduleSys.arecordTest()
    #moduleSys.cpuTempCheck(20, 60)


def U7150(sCPU, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.snGet(pn, modelName)
    moduleSys.dmidecodeLog("bios-version")
    moduleSys.dmidecodeLog("baseboard-product-name")
    moduleSys.dmidecodeLog("baseboard-serial-number")
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    #moduleSys.memoryGet()
    moduleSys.memoryCheck("4096","4096")
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanCheck("eth0", "80:7b:85")
    moduleSys.lanCheck("eth1", "00:13:95")
    moduleSys.usbCheck("Keyboard", 1)
    moduleSys.usbCheck("Mouse", 1)
    moduleSys.usbCheck("JMS567", 1)
    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
    moduleCg.i2cGpio()
    moduleSys.uartLoop("/dev/ttyS5")
    moduleSys.aplayTest()
    moduleSys.arecordTest()
    #moduleSys.cpuTempCheck(20, 60)


def U6500(sCPU):
    print("Not Ready")


def debug(sCPU, sPoe, sFan, sDio, sLan, sCom, sDisk):
    modelName = inspect.currentframe().f_code.co_name
    moduleSys.funcMenu()
    moduleSys.snGet(pn, modelName)
    #moduleSys.biosVersionCheck("1.20")
    #testBi.biStressRoom()
    moduleSys.biosReleaseCheck("11/11/2020")
    moduleEbk.aicVersion("AIC-1.04")
    moduleEbk.aicDdmLogo()
    moduleEbk.aicTemp(20, 60)
    moduleEbk.aicRtc(2.999, 3.333)
#    moduleEbk.aicPoe(sPoe)
#    moduleEbk.aicFan(sFan)
    moduleEbk.aicDioSelect(sDio)
    moduleSys.rtcCheck("withBat")
    moduleSys.cpuCheck(sCPU)
    moduleSys.memoryGet()
    moduleSys.storageCheck(sDisk)
    moduleSys.storageGet()
    moduleSys.lanSpeedSet(sLan, 100)
    moduleSys.lanLedCheckAll()
#    moduleSys.lanSelect(sLan)
#    moduleSys.usbCheck("Keyboard", 1)
#    moduleSys.usbCheck("JMS567", 1)
#    moduleSys.usbCheck("DataTraveler|JetFlash", 1)
#    moduleSys.usbCheck("Converter|Chic|Scanner|Metrologic|FUZZYSCAN", 1)
#    moduleSys.uartLoopCheck(sCom)
#    moduleSys.alsabatTest()
#    testBi.biStressCheck()
    #moduleSys.cpuTempCheck(20, 60)

def default():
    print(" ")
    print(Fore.MAGENTA + Back.WHITE)
    print("此PN無對應測試程式")
    print(Style.RESET_ALL)
    check = input("按任意鍵繼續 press any key continue...").lower()
    with open(startTest, "w") as f:
        f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
    subprocess.call("sh %s" % startTest, shell=True)


os.system('clear')
print(" ")
print(Fore.BLUE + Back.WHITE)
print("組裝測試選單 ASSY-MENU" + Style.RESET_ALL, end='')
print(" Build by EFCO SamLee明")
print(Fore.MAGENTA + Back.WHITE)
print("測試PN:", pn)
print(Style.RESET_ALL)

#AIMH
#DIO=GPIO1 IDIO=DIO1
#1-CPU, Poe, fan, dio, Lan, Com, Disk
#U7XXX
#1-CPU, Disk
if pn == "10300-000000-A.0": debug("6500", 4, 2, "1D", 6, 6, "opCheck")
elif pn == "10300-000004-A.3": Q715QA5OS("withBat")
elif pn == "10300-000004-A.4": Q715QA5OS("withBat")
elif pn == "10300-000007-A.0": Q715QA5OS("withoutBat")
elif pn == "10300-000008-A.0": CJB("cpu", "disk")
elif pn == "10400-000004-B.2": U7130PAS("NA")
elif pn == "10400-000009-A.0": U7150("N4200")
elif pn == "10400-000010-A.0": U7150("N4200")
elif pn == "10500-000340-A.0": U7130("N2870", "59.6G")
elif pn == "10902-000097-A.0": AIM("6300", 4, "noFan", "1I", 4, 4, "opCheck")
elif pn == "10951-000004-A.0": U7130("NA")
elif pn == "10953-000001-B.0": U650("NA")
elif pn == "20010-000160-A.0": AIM("6600", 4, "noFan", "1I", 4, 4, "opCheck")
elif pn == "20010-000161-A.0": AIM("6300", 4, "noFan", "1I", 4, 4, "opCheck")
elif pn == "20010-000162-A.0": AIM("6100", 4, "noFan", "1I", 4, 4, "opCheck") #AIM
elif pn == "20010-000170-A.0": AIH("NA", 4, 2, "1D2D", 6, 2)
elif pn == "20010-000173-A.1": AIM("6600", 0, "noFan", "1I", 2, 4, "opCheck") #AIML-I
elif pn == "20010-000177-A.1": AIM("6300", 0, "noFan", "1I", 2, 4, "opCheck") #AIML-I
elif pn == "20010-000179-A.1": AIM("3955", 0, "noFan", "1I", 2, 4, "opCheck") #AIML-I
elif pn == "20010-000181-A.2": AIH("NA", 4, 2, "1I2I", 6, 2, "opCheck") #AIHDP-i2
elif pn == "20010-000191-A.1": AIM("7300", 0, "noFan", "1I", 2, 4, "opCheck") #AIML-I
elif pn == "20010-000194-A.2": AIH("NA", 4, "noFan", "1D", 6, 6, "opCheck") #AIH-DIO
elif pn == "20010-000197-A.1": AIH("NA", 4, 2, "1D", 6, 6, "opCheck") #AIH-EP1
elif pn == "20010-000199-A.1": AIH("NA", 4, 2, "1I2D", 6, 2, "opCheck") #AIHDP-i
elif pn == "20010-000238-A.1": AIM("6100", 0, "noFan", "1D", 2, 4, "opCheck") #AIML-D
elif pn == "20010-000263-A.1": AIM("6600", 4, "noFan", "1I", 6, 2, "opCheck") #AIMG6
elif pn == "20010-000294-A.1": AIH("NA", 0, "NoFan", "1I", 2, 6, "opCheck") #AIHL-I
elif pn == "20010-000303-A.1": AIH("NA", 4, 2, "1I2D", 6, 2, "opCheck") #AIHD-P4E2-i
elif pn == "20010-000327-A.0": AIM("7200", 4, "noFan", "1I", 4, 2, "opCheck") #AIMD7
elif pn == "20010-000335-A.0": U7130("N2807", "opCheck")
elif pn == "20010-000355-A.0": U7150("N4200", "opCheck")
elif pn == "20010-000401-A.0": AIM("7600", 4, "noFan", "1I", 6, 2, "opCheck") #AIMG7
elif pn == "20010-000404-A.1": AIM("7200", 0, "noFan", "1I", 2, 4, "opCheck") #AIML-I
elif pn == "20010-000407-A.0": AIM("7200", 0, "noFan", "1D", 2, 4, "opCheck") #AIML-D
else: default()

moduleSys.passGreen()

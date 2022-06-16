#!/bin/python3
#from subprocess import Popen, PIPE
import serial
import re
import logging
import subprocess
import enquiries
import sys
import os
import time
import usb.util
import pexpect
#sys.path.append("..")
from pyFunc import moduleSys
from pyFunc import moduleEbk
from pyFunc import moduleCg
import json
import shelve
import scp
from paramiko import SSHClient
from scp import SCPClient

hostName = "10.0.0.6"
hostFolder = "C:"
localFolder = "/home/partimag/log"
response = os.system("ping -c 1 " + hostName)
if response == 0:
    subprocess.call(
            "sshpass -p efco1234 scp -o StrictHostKeyChecking=no -r %s production@%s:%s"
            % (localFolder, hostName, hostFolder), shell=True)

    #ssh = SSHClient()
    #ssh.load_system_host_keys()
    #ssh.connect('10.0.0.6')
    #scp = SCPClient(ssh.get_transport())
    #scp.put('example.txt', 'example2.txt')
    #scp.put('/home/partimag/log', recursive=True, remote_path='C:')
    #scp.get('example2.txt')
else:
    print ("ping fail " + hostName )
    time.sleep(5)

def scpCheck():
    host = "10.0.0.6"
    user = "production"
    client = scp.Client(host=host, user=user, keyfile=keyfile)
    # or
    client = scp.Client(host=host, user=user)
    client.use_system_keys()
    # or
    client = scp.Client(host=host, user=user, password=password)
    # and then
    client.transfer('/etc/local/filename', '/etc/remote/filename')


scpCheck()

#Get PN from db
#with shelve.open('/home/stux/pyPackage/dataBase') as db:
#    pn = db['pnSave']
pn = "test"
modelName = "test"
moduleSys.snGet(pn, modelName)

#moduleSys.lanNicCheck(1, "001395") # Check CPU NIC MAC
#moduleSys.lanEepromCheck(2, "3.25") # Check NIC Eeprom revision
#moduleSys.lanMacProg(2, "807B85")
#moduleCg.i2cGpio()
#moduleSys.uartLoop("/dev/ttyS0")
#moduleSys.memoryCheck("8192 MB","No Module")
#moduleEbk.aicFan(2)
moduleEbk.aicDioSelect("1I2D")
#moduleEbk.aicDio("GPIO1")
#moduleEbk.aicIdioConfig("DIO1", "SINK")
#moduleEbk.aicIdioCheck("DIO1")
#moduleEbk.aicIdioConfig("DIO1", "SOURCE")
#moduleEbk.aicIdioCheck("DIO1")
#moduleEbk.aicIdioConfig("DIO1", "SOURCE")
#moduleEbk.aicIdioConfig("DIO2", "SINK")
#moduleEbk.aicIdioConfig("DIO2", "SOURCE")




def getCpuTemp():
    #sensor -j > json type
    sensors = subprocess.check_output(
            "sensors -j", shell=True) 
    sensors = json.loads(sensors)
    cpuT = sensors['coretemp-isa-0000']['Core 0']['temp2_input']
    cpuT = int(float(cpuT))
    print(cpuT)
    return cpuT

#getCpuTemp()

def atCheck(comPort, atCommand, atBack):
    atLog = "/tmp/at.log"
    if os.path.exists(atLog):
        os.remove(atLog)
    subprocess.call("sudo cat %s | tee -a %s &" % (comPort, atLog), shell=True, timeout=5)
    try:
        subprocess.call("sudo sh -c \"echo '%s' > %s\"" % (atCommand, comPort), shell=True, timeout=5)
    except:
        logging.error('AT_COMMAND: %s %s get failed!' % (comPort, atCommand))
        failRed("%s AT Command 連線失敗" % atCommand)
    time.sleep(2)
    with open(atLog) as f:
        lines = f.read()
    print(lines)
#    lines = str(lines)
    print(lines)
    if re.search(atBack, lines):
        print("OKOK")
        logging.info(atCommand + ': ' + lines + " SPEC: " + atBack)
        return True

    #else:
#        logging.error(atCommand + ': ' + lines + " SPEC: " + atBack)
#        failRed("確認 LTE & SIM 卡" + atCommand)
    subprocess.call("sudo killall cat &", shell=True, timeout=5)



#atCheck("/dev/ttyUSB2", "at\r\n", "OK")


def uartLoopCheck(comPort):
    subprocess.call("sudo chmod 666 %s" % comPort, shell=True )

    mySerial = serial.Serial(comPort, 115200, timeout=1)
    sendData = "at\r\n"
    result = mySerial.write(sendData.encode())
    time.sleep(3)
    recvData = mySerial.readline()
    print("Data" + recvData)
    for num  in range(1, 6):
        sendData = bytes([num])
        result = mySerial.write(sendData)
        recvData = mySerial.readline()
        if sendData != recvData:
            logging.error('Tese_UART: %s loopback test failed!' % comPort)
            failRed("%s COM PORT LOOPBACK測試失敗" % comPort)
            print('test fail')
        print('COM PORT LOOPBACK TEST %s' % num)
#    logging.info('Test_UART: %s loopback test passed!' % comPort)

#uartLoopCheck("/dev/ttyUSB2")

def diskChoose():
    deviceModel = 'USB3.0'
    output = subprocess.check_output(
            'lsblk -o name,model', shell=True)
    output = str(output).lstrip('b\'').split('\\n')
    for line in output:
        if re.search(deviceModel, line):
            print(line)
    diskGet = 0

diskChoose()

def sizeCheck():
    output = subprocess.check_output(
            'lsblk /dev/%s1 -o size' % diskGet, shell=True)
    print(output)
    output = str(output).lstrip('b\'').split('\\n')
    part1 = output[1].lstrip()
    if part1 == "2G":
        print("2G OK")
        print(part1)
    else:
        print("2G NG")
        print(part1)


def osSync():
    diskChoose()
    subprocess.check_call("sudo mount /dev/%s2 /mnt -o umask=000" % diskGet, shell=True, stdin=sys.stdin)
    subprocess.check_call("sudo rsync -avh /home/partimag/OS_IMAGE /mnt", shell=True, stdin=sys.stdin)
    subprocess.check_call("sudo umount /mnt", shell=True, stdin=sys.stdin)

#diskChoose()
#print(diskGet)
#sizeCheck()

#print('filename: ' + __file__)

#moduleSys.uartLoopCheck("/dev/ttyS0", "1")
#moduleEbk.aicIdio("DIO1", 00)
#moduleSys.uartLoopCheck("/dev/ttyS0", "1")
#sCom = 4
#if sCom == 4:
#    for i in range(sCom):
#        j = i + 1
#        print(i)
    #moduleSys.uartLoopCheck("/dev/ttyS%s" % i, "%s" % j)

#help(usb)
#moduleSys.usbCheck("Hub")
#moduleSys.usbCheck("Keyboard|hub", 1)

#dev = usb.core.find(find_all=True)
#for cfg in dev:
#    print(cfg.iManufacturer)
#    print(usb.util.get_string(cfg, 1))
    #print(cfg.manufacturer)
#    print('Product_name=' + str(cfg.iManufacturer) + '\n')
#    print('Product_name=' + str(cfg.iProduct) + '\n')
#    print("123= ", usb.util.get_string(cfg, 256, 2))

#process = pexpect.spawn('df -h')
#process.logfile = sys.stdout
#print(process.read('sda1'))
#print(process.read())
#print(process.expect(pexpect.EOF))




#moduleSys.getCpuMips()
#print(n)



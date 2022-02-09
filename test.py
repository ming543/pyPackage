#!/bin/python3
#from subprocess import Popen, PIPE
import subprocess
import enquiries
import sys
import os
import usb.util
import pexpect
#sys.path.append("..")
from pyFunc import moduleSys
from pyFunc import moduleEbk


def diskChoose():
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
    global diskGet
    diskGet = diskShow.split(' ')[1]

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

diskChoose()
#print(diskGet)
sizeCheck()

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


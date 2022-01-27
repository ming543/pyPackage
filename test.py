#!/bin/python3
#from subprocess import Popen, PIPE
import sys
import usb.util
import pexpect
#sys.path.append("..")
from pyFunc import moduleSys
from pyFunc import moduleEbk


#print('filename: ' + __file__)

#moduleSys.uartLoopCheck("/dev/ttyS0", "1")
moduleEbk.aicIdio("DIO1", 00)


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


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import cgos as cg
cg.openif()

ulUnit = 0
usGpioHwFail = True
cg.ioWrite(ulUnit, 0x00000000)
ulGPIOPinState = cg.ioRead(ulUnit)
print ("spec = 0x0, get " + hex(ulGPIOPinState))
if (ulGPIOPinState & 0x000000FF) == 0x00000000:
    cg.ioWrite(ulUnit, 0x00000010)
    ulGPIOPinState = cg.ioRead(ulUnit)
    print ("spec = 0x11, get " + hex(ulGPIOPinState))
    if (ulGPIOPinState & 0x000000FF) == 0x00000011:
        cg.ioWrite(ulUnit, 0x00000020)
        ulGPIOPinState = cg.ioRead(ulUnit)
        print ("spec = 0x22, get " + hex(ulGPIOPinState))
        if (ulGPIOPinState & 0x000000FF) == 0x00000022:
            cg.ioWrite(ulUnit, 0x00000040)
            ulGPIOPinState = cg.ioRead(ulUnit)
            print ("spec = 0x44, get " + hex(ulGPIOPinState))
            if (ulGPIOPinState & 0x000000FF) == 0x00000044:
                cg.ioWrite(ulUnit, 0x00000080)
                ulGPIOPinState = cg.ioRead(ulUnit)
                print ("spec = 0x88, get " + hex(ulGPIOPinState))
                if (ulGPIOPinState & 0x000000FF) == 0x00000088:
                    cg.ioWrite(ulUnit, 0x000000F0)
                    ulGPIOPinState = cg.ioRead(ulUnit)
                    print ("spec = 0xff, get " + hex(ulGPIOPinState))
                    if (ulGPIOPinState & 0x000000FF) == 0x000000FF:
                        usGpioHwFail = False
                        print ("\nAutomatic COMExpress GPIO hardware test successful!")
                        cg.closeif()
                        exit(0)
if usGpioHwFail == True: print ("\nERROR: Automatic COMExpress GPIO hardware test failed!")
cg.closeif()
exit(1)




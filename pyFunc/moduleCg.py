#!/bin/python3
import os
import getmac
import cgos as cg

def cgTest():
    cg.openif()
    result = cg.boardGetInfo()
    print (result)
    print (result['szSerialNumber'])

    pyFolder = "/home/stux/pyPackage/"
    cgFolder = pyFolder + "tools/CgosPy_1_2"

def i2cGpio():
    gpio = "/home/stux/pyPackage/tools/cgoslx-gpio/CgosI2cGpio/Lx/cgosi2c_gpio"
    response = subprocess.check_output(gpio, shell=True)
    response = sesponse.splitlines()
    print(response)
    if re.search('input:80', response):
        logging.info('GPIO Loopback Test : PASS')
        return True
    else:
        logging.error('GPIO Loopback Test : Fail ' + response[0] ' SPEC: 80')
        failRed("GPIO Loopback test Fail " + response[0])
    
        
    

#!/bin/python3
#from subprocess import Popen, PIPE
import sys
import pexpect
#sys.path.append("..")
from pyFunc import moduleSys

#print('filename: ' + __file__)

process = pexpect.spawn('df -h')
#process.logfile = sys.stdout

#print(process.read('sda1'))
print(process.read())
print(process.expect(pexpect.EOF))




#moduleSys.getCpuMips()
#print(n)


#!/bin/python3
import git
import os
# import sys
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
from colorama import Fore
import pexpect

pyFolder = "/home/stux/pyPackage/"
ekitFolder = pyFolder + "tools/EKit_L"

def aic():
    process = pexpect.spawn('df -h')
    print(process.expect(pexpect.EOF))
    #i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
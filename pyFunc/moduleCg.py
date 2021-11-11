
import os
import getmac

loc="/home/production"
logPath = loc + "/log"
print(logPath)
pn = "10953-000001-B.0\\" #pn for U6-500

def macCheck(macA):
    ethMac = getmac.get_mac_address(interface = macA)
    print (ethMac)

os.system('clear')
print("Test Start, input SN")
snGet = input()

macCheck("enp1s0")
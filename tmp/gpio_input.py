#!/bin/python3
import os
os.environ.setdefault('BLINKA_FT232H', '1')
import board
import digitalio
import time

C0 = digitalio.DigitalInOut(board.C0)
C1 = digitalio.DigitalInOut(board.C1)
C2 = digitalio.DigitalInOut(board.C2)
C3 = digitalio.DigitalInOut(board.C3)
C4 = digitalio.DigitalInOut(board.C4)
C5 = digitalio.DigitalInOut(board.C5)
C6 = digitalio.DigitalInOut(board.C6)
C7 = digitalio.DigitalInOut(board.C7)

#nameList = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']

#C0.direction = digitalio.Direction.INPUT
for i in range(8):
#    print('print: ', locals()['C' + str(i)])
    locals()['C' + str(i)].direction = digitalio.Direction.INPUT


count = 0
while count < 30:
    time.sleep(1)
    os.system('clear')
    startTime = time.strftime("%H%M%S", time.localtime())
    print('Check FT232H GPIO status... ' + startTime)
    for i in range(8):
        print('The GPIO Port %s: ' % i, end='' )
        print(str(locals()['C' + str(i)].value))
    
    count = count + 1
    print(' ')
    print('Test end at count 30, now is %s' % count)




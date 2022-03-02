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
import numpy as np
import pyaudio

# logging.basicConfig(level=logging.DEBUG)
# log_filename = datetime.datetime.now().strftime(sn + "-%Y-%m-%d-%H:%M:%S.log")
# logging.basicConfig(level=logging.INFO)

# Check system boot by UEFI or LEGACY mode
booted = "UEFI" if os.path.exists("/sys/firmware/efi") else "LEGACY"

# Get revision
g = git.Git('.')
loginfo = g.log('-m', '-1', '--pretty=format:"%h %s"')


#sT = "/home/production/pyPackage/t.sh"
startTest = "/home/stux/pyPackage/t.sh"
logPath = "/home/partimag/log/"
if os.path.isdir(logPath):
    print(" ")
else:
    subprocess.check_call("sudo mount /dev/sda2 /home/partimag -o umask=000", shell=True)

def audioPlay():
    #隱藏一些報錯，這些不影響程式的執行
    os.close(sys.stderr.fileno())
    frequency=1000
    t=3
    sampleRate=44100
    # 播放數量
    n = int(t * sampleRate)
    # 每秒轉動的角度再細分為取樣間隔
    interval = 2 * np.pi * frequency / sampleRate
    data = np.sin(np.arange(n) * interval)
    # 因 format 為  pyaudio.paFloat32，故轉換為 np.float32 並轉換為 bytearray
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=True)
    stream.write(data.astype(np.float32).tostring())
    stream.close()
    p.terminate()

def audioWire():
    """
    PyAudio Example: Make a wire between input and output (i.e., record a
    few samples and play them back immediately).
    """
    CHUNK = 1024
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

    print("* recording")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()
    
    
        
def atCheck(comPort, atCommand, atBack):
    atCommandrn = atCommand + '\\r\\n'
    atLog = "/tmp/at.log"
    if os.path.exists(atLog):
        os.remove(atLog)
    subprocess.call("sudo cat %s | tee -a %s &" % (comPort, atLog), shell=True, timeout=5)
    try:
        subprocess.call("sudo sh -c \"echo '%s' > %s\"" % (atCommandrn, comPort), shell=True, timeout=5)
#        for i in range(2):
#            subprocess.call("sudo sh -c \"echo '%s' > %s\"" % (atCommandrn, comPort), shell=True, timeout=5)
#            time.sleep(2)
    except:
        subprocess.call("sudo killall cat &", shell=True, timeout=5)
        logging.error('AT_COMMAND: %s %s get failed!' % (comPort, atCommand))
        failRed("%s AT Command 連線失敗" % atCommand)
    with open(atLog) as f:
        lines = f.readlines()
    lineCheck = False
    for i in range(len(lines)):
        if re.search(atBack, lines[i]):
            linesRn = lines[i].rstrip()
            logging.info("%s: %s" % (atCommand, linesRn))
            lineCheck = True
            break
    if lineCheck == False:
            subprocess.call("sudo killall cat &", shell=True, timeout=5)
            logging.error(atCommand + ": not find. SPEC: " + atBack)
            failRed("確認 LTE & SIM 卡 " + atCommand) 
    subprocess.call("sudo killall cat &", shell=True, timeout=5)
    time.sleep(2)


def cpuTempCheck(cpuL, cpuH):
    sensors = subprocess.check_output(
            "sensors -u", shell=True)
    sensors = sensors.decode().splitlines()
    for line in sensors:
        if re.search('temp2_input', line):
            cpuT = str(f'{line}').split(':')[1]
            cpuT = int(float(cpuT))
    if cpuL < cpuT < cpuH:
        logging.info("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
    else:
        logging.error("Check CPU temp %s ! spec %s to %s C" % (cpuT, cpuL, cpuH))
        failRed("確認 CPU 溫度 %s C ! spec %s to %s C" % (cpuT, cpuL, cpuH))

def pnGet():
    print(Fore.YELLOW + " 選取測試PN " + Fore.RESET, end='')
    print(Fore.YELLOW + " Choose PN number for Test and Log! " + Fore.RESET)
    index = ['10300-', '10400-', '10500-', '10901-', '10902-', '10951-', '10953-', '20010-']
    indexChoice = enquiries.choose('  Choose options: ', index)
    body = []
    for i in range(0, 10):
        #add number by six digi, someday may used.
        #body.append(indexChoice + "{:06d}".format(i))
        body.append(indexChoice + '000' + str(i))
    bodyFirst = enquiries.choose(' Choose body: ', body)
    body.clear()
    for j in range(0, 10):
        body.append(bodyFirst + str(j))
    bodySecond = enquiries.choose(' Choose body: ', body)
    body.clear()
    for k in range(0, 10):
        body.append(bodySecond + str(k))
    bodyThird = enquiries.choose(' Choose body: ', body)
    body.clear()
    rev = [bodyThird + '-A.', bodyThird + '-B.', bodyThird + '-C.', bodyThird + '-D.', bodyThird + '-E.']
    revChoice = enquiries.choose('  Choose Revision: ', rev)
    for p in range(0, 10):
        body.append(revChoice + str(p))
    pn = enquiries.choose('  Choose PN: ', body)
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['pnSave'] = pn

def pnGet2():
    index = []
    aPath = "/home/stux/pyPackage/testAssy"
    print(Fore.YELLOW + "%s ASSY-MENU" % booted + Fore.RESET, end='')
    print(" Build by EFCO SamLee")
    print("Revision %s" % loginfo)
    for filename in os.listdir(aPath):
        index += [filename]
    choice = enquiries.choose('  Choose options: ', index)
    for i in range(len(index)):
        if choice == index[i]:
            return index[i]


def pnCheck():
    os.system('clear')
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        pn = db['pnSave'] 
    print(Fore.YELLOW + "確認PN是否正確" + Fore.RESET, end='')
    print(Fore.YELLOW + " Check PN number for Test and Log! " + Fore.RESET)
    print("Test_PN: " + pn)
    pnCheck = input("任意鍵繼續 Press any key continue: ").lower()
    if pnCheck == "n":
        return False
    else:
        return True


# pn input form script
def snGet(pn, modelName):
#    os.system('clear')
    print("Test_Model: " + modelName)
#    print("Test_PN: " + pn)
    print("按n鍵結束  ", end='')
    print("Back to menu press 'n' ")
    print(Fore.YELLOW + "輸入序號開始測試 " + Fore.RESET, end='')
    print(Fore.YELLOW + "Input SN start test: " + Fore.RESET)
    global sn
    sn = input()
    sn = str(sn)
    #with shelve.open('snTemp') as db:
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['snSave'] = sn

    if sn == "n":
        print("Start Test is " + startTest)
        with open(startTest, "w") as f:
            f.write("cd /home/stux/pyPackage && python3 pyMenu.py")
        subprocess.call("sh %s" % startTest, shell=True)
    else:
        # setup test start time
        startTime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        # setup test log month folder
        logMonth = time.strftime("%Y%m", time.localtime())
        logFilename = sn + "-" + modelName + "-" + startTime + ".log"
        global log
        log = logPath + pn + "/" + logMonth + "/" + logFilename
        os.makedirs(os.path.dirname(log), exist_ok=True)  # Create log folder
        # save log name and location to database
        # with shelve.open('snTemp') as db:
        with shelve.open('/home/stux/pyPackage/dataBase') as db:
            db['log'] = log

        logger = logging.getLogger()
        # Setup logging level
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                datefmt='%Y%m%d %H:%M:%S')

        # Setup log show on stream and file both
        ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        # log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        # fh = logging.FileHandler(log_filename)
        fh = logging.FileHandler(log)
        # fh.setLevel(logging.DEBUG)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)
        logging.info('Test_Model: ' + modelName)
        logging.info('Test_PN: ' + pn)
        logging.info('Test_SN: ' + sn)
        # logging.debug('debug')
        # logging.info('info')
        # logging.warning('warning')
        # logging.error('error')
        # logging.critical('critical')
    return sn

#dmiFunc ex.baseboard-product-name
def dmidecodeCheck(dmiFunc, spec):
    biosN = subprocess.check_output("sudo dmidecode -s %s" % dmiFunc, shell=True)
    biosN = str(biosN)
    if re.search(spec, biosN):
        logging.info(dmiFunc + ': ' + biosN + " SPEC: " + spec)
        return True
    else:
        logging.error(dmiFunc + ': ' + biosN + " SPEC: " + spec)
        failRed("規格不符")		


def dmidecodeLog(dmiFunc):
    biosN = subprocess.check_output("sudo dmidecode -s %s" % dmiFunc, shell=True)
    biosN = str(biosN).lstrip('b\'').split('\\n')[0]
    logging.info(dmiFunc + ': ' + biosN)
    return True
    
        

def biosVersionCheck(spec):
    biosV = subprocess.check_output("sudo dmidecode -s bios-version", shell=True)
    biosV = str(biosV).lstrip('b\'').split('\\n')[0]
    if re.search(spec, biosV):
        logging.info('BIOS_Version: ' + biosV + " SPEC: " + spec)
    else:
        logging.error('BIOS_Version: ' + biosV + " SPEC: " + spec)
        failRed("BIOS版本不符")


def biosReleaseCheck(spec):
    biosV = subprocess.check_output("sudo dmidecode -s bios-release-date", shell=True)
    biosV = str(biosV).lstrip('b\'').split('\\n')[0]
    if re.search(spec, biosV):
        logging.info('BIOS_Release_Date: ' + biosV + " SPEC: " + spec)
    else:
        logging.error('BIOS_Release_Date: ' + biosV + " SPEC: " + spec)
        failRed("BIOS_Release_Date不符")


def rtcCheck():
    y = "2022"  # check years of BIOS time
    rtcTime = subprocess.check_output("sudo hwclock -r", shell=True)
    rtcTime = str(rtcTime).lstrip('b\'').split('\\n')[0]
    if re.search(y, rtcTime):
        logging.info('RTC_Time: ' + rtcTime + " SPEC: " + y)
    else:
        logging.error('RTC_Time: ' + rtcTime + " SPEC: " + y)
        failRed("rtc年份不符")


def lanMacCheck(ethN, macH):
    ethMac = getmac.get_mac_address(interface=ethN)
    if re.search(macH, ethMac):
        logging.info('Test_MAC: ' + ethN + "_" + ethMac + " SPEC: " + macH)
    else:
        logging.error('Test_MAC: ' + ethN + "_" + ethMac + " SPEC: " + macH)
        failRed("MAC不符")


def lanCheck(ethN, macH):
    #test MAC
    ethMac = getmac.get_mac_address(interface=ethN)
    if re.search(macH, ethMac):
        logging.info('Test_MAC: ' + ethN + " " + ethMac + " SPEC: " + macH)
    else:
        logging.error('Test_MAC: ' + ethN + " " + ethMac + " SPEC: " + macH)
        failRed("MAC不符")
    #test carrier link
    response = subprocess.check_output(
            "cat /sys/class/net/%s/carrier" % ethN, shell=True)
    response = str(response).lstrip('b\'').split('\\n')[0]
    if response == "1":
        logging.info('Test_Lan: %s carrier linked' % ethN)
    else:
        logging.error('Test_Lan: %s carrier not link' % ethN)
        failRed("%s 測試網路連線失敗" % ethN)
    #test IP get
    try:
        ipAddr = netifaces.ifaddresses(ethN)[netifaces.AF_INET]
        ipAddr = ipAddr[0]['addr']
        logging.info('Test_Lan: %s IP address: %s' % (ethN,ipAddr))
    except KeyError: 
        print("keyerror")
        logging.error('Test_Lan: %s IP address get failed!' % ethN)
        failRed("%s 測試網路IP連線失敗" % ethN)

def lanSpeedSet(sLan, sSpeed):
    for i in range(sLan):
        subprocess.call(
            "sudo ethtool -s eth%s speed %s duplex full autoneg on" % (i, sSpeed), shell=True )
        subprocess.call(
            "ping 8.8.8.8 -c 20 > /dev/null &", shell=True )
    logging.info('LAN_SPEED_SET: eth%s to %s' %(i, sSpeed))

    
def lanLedCheck(ledL, ledR):
    os.system('clear')
    print(" ")
    print("網路燈號確認 LAN LED Check")
    print("確認網路孔燈號是否顯示 - %s %s" % (ledL, ledR))
    print(" ")
    print("不良按n鍵結束,其他鍵繼續  ", end='')
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('LAN_LED_ON: Not display as normal')
        failRed("LAN LED 燈號不良")
    logging.info('LAN_LED_ON: Display OK')


def lanLedOffCheck(ledL, ledR):
    os.system('clear')
    print(" ")
    print("網路燈號確認 LAN LED OFF Check")
    print("移除網路線 Remove LAN Cable")
    print("確認網路孔燈號是否顯示 - %s %s" % (ledL, ledR))
    print(" ")
    print("不良按n鍵結束,其他鍵繼續  ", end='')
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('LAN_LED_OFF: Not display as normal')
        failRed("LAN LED_OFF 燈號未熄滅")
    logging.info('LAN_LED_OFF: Remove LAN Cable and LED OFF')


def usbCheck(spec, num):
    usbList = subprocess.check_output("lsusb", shell=True)
    usbSplit = str(usbList).lstrip('b\'').rstrip('\'').split('\\n')
    usbNum = 0
    for i in range(len(usbSplit)-1):
        if re.search(spec, str(usbSplit[i])):
            #logging.info( 'Check USB %s OK: ' % spec + usbSplit[i])
            usbNum += 1
    if usbNum == num:
        logging.info( 'Check USB %s x %s SPEC: %s ' % (spec, usbNum, num))
    else:
        for i in range(len(usbSplit)-1):
            logging.error('Check USB %s x %s Fail! SPEC: %s ' % (spec, usbNum, num) + usbSplit[i] )
        failRed("Check USB %s x %s 規格不符 SPEC: %s " % (spec, usbNum, num))		


def uartLoopCheck(comPort, num):
    os.system('clear')
    print(" ")
    print("COM LOOPBACK 單一接頭測試 ")
    print("確認 LOOPBACK 位於 COM - %s" % num)
    print(" ")
    input("按任意鍵繼續 Press any key continue...")
    subprocess.call("sudo chmod 666 %s" % comPort, shell=True )
    mySerial = serial.Serial(comPort, 115200, timeout=1)
    for num  in range(1, 6):
        sendData = bytes([num])
        result = mySerial.write(sendData)
        recvData = mySerial.readline()
        if sendData != recvData:
            logging.error('Tese_UART: %s loopback test failed!' % comPort)
            failRed("%s COM PORT LOOPBACK測試失敗" % comPort)
            print('test fail')
        print('COM PORT LOOPBACK TEST %s' % num)
    logging.info('Test_UART: %s loopback test passed!' % comPort)





def failRed(issueCheck):
    logging.error('****** TEST_FAILED! ******')
    logFail = log + ".FAIL"
    os.replace(log, logFail)
    print(Fore.RED + "FFFFFF______A______IIIIII____LL____" + Fore.RESET)
    print(Fore.RED + "FF_______AA___AA_____II______LL____" + Fore.RESET)
    print(Fore.RED + "FFFF_____AA___AA_____II______LL____" + Fore.RESET)
    print(Fore.RED + "FF_______AA___AA_____II______LL____" + Fore.RESET)
    print(Fore.RED + "FF_______AA_A_AA_____II______LL____" + Fore.RESET)
    print(Fore.RED + "FF_______AA___AA___IIIIII____LLLLLL" + Fore.RESET)
    print(" ")
    print("測試序號SN:", sn)
    print("確認規格:", issueCheck)
    print(" ")
    print("按n鍵關機,其他鍵重測  ", end='')
    check = input("Press'n'power off, other key re-test: ").lower()
    if check == ("n"):
        os.system('systemctl poweroff')
    subprocess.call("sh %s" % startTest, shell=True)


def passGreen():
    logging.info('****** TEST_PASSED! ******')
    logPass = log + ".PASS"
    os.replace(log, logPass)
    print(Fore.GREEN + "PPPPP_______A______SSSSSS___SSSSSS" + Fore.RESET)
    print(Fore.GREEN + "PP__PP____AA_AA____SS_______SS____" + Fore.RESET)
    print(Fore.GREEN + "PP___PP__AA___AA___SS_______SS____" + Fore.RESET)
    print(Fore.GREEN + "PP__PP___AA___AA___SSSSSS___SSSSSS" + Fore.RESET)
    print(Fore.GREEN + "PPPPP____AA___AA_______SS_______SS" + Fore.RESET)
    print(Fore.GREEN + "PP_______AA_A_AA_______SS_______SS" + Fore.RESET)
    print(Fore.GREEN + "PP_______AA___AA___SSSSSS___SSSSSS" + Fore.RESET)
    print(" ")
    print("按任意鍵關機  ", end='')
    check = input("Press any key power off").lower()
    if check == ("n"):
        subprocess.call("sh %s" % startTest, shell=True)
    os.system('systemctl poweroff')



def cpuGet():
    os.system('clear')
    c = cpuinfo.get_cpu_info()['brand_raw']
    print("CPU_Info: " + c)
    print(Fore.YELLOW + "確認CPU型號與BOM是否相符 " + Fore.RESET, end='')
    print(Fore.YELLOW + "Check CPU with BOM" + Fore.RESET)
    print("按n鍵結束,其他鍵繼續  ", end='')
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('CPU_Info: ' + c + ' not match BOM')
        failRed("CPU型號不符")
    logging.info('CPU_Info: ' + c)


def memoryGet():
    os.system('clear')
    memoryA = subprocess.check_output(
            "sudo dmidecode -t memory | grep 'ChannelA\|Size\|Part\|Serial'", shell=True)
    memoryA = str(memoryA).lstrip('b\'\\t').rstrip('\\n\'').split('\\n\\t')
    memoryB = subprocess.check_output(
            "sudo dmidecode -t memory | grep 'ChannelB\|Size\|Part\|Serial'", shell=True)
    memoryB = str(memoryB).lstrip('b\'\\t').rstrip('\\n\'').split('\\n\\t')
    for i in range(4):
        logging.info('Memory_A ' + memoryA[i])
    print(" ")
    try:
        for i in range(4):
            logging.info('Memory_B ' + memoryB[i])
        print(" ")
    except:
        logging.info('Memory_B not find')
        print(" ")

    print(Fore.YELLOW + "確認記憶體規格與BOM是否相符 " + Fore.RESET, end='')
    print(Fore.YELLOW + "Check Memory with BOM" + Fore.RESET)
    print("按n鍵結束,其他鍵繼續  ", end='')
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('Memory_Info: not match BOM')
        failRed("記憶體規格不符")
    

def storageGet():
    os.system('clear')
    output = subprocess.check_output(
            'lsblk -o type,name,model,size', shell=True)
    output = str(output).lstrip('b\'').split('\\n')
    options = []
    for line in output:
        if line.lower().startswith('disk'):
            options.append(line)
    check = False
    for i in range(1, len(options)):
        logging.info('Storage_Info: ' + options[i])
        check = True
    if check == False:
        print("系統查無儲存裝置 No storage find at system")
    print(Fore.YELLOW + "確認儲存裝置與BOM是否相符 " + Fore.RESET, end='')
    print(Fore.YELLOW + "Check Storage with BOM" + Fore.RESET)
    print("按n鍵結束,其他鍵繼續  ", end='')
    check = input("Failed press 'n', other key continue: ").lower()
    if check == ("n"):
        logging.error('Storage_Info: not match BOM')
        failRed("儲存裝置規格不符")


def diskGet():
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
    diskGet = diskShow.split(' ')[1]
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['diskSave'] = diskGet
        db['diskShow'] = diskShow


def osGet():
    os.system('clear')
    index = []
    osFolder = "/home/partimag/OS_IMAGE"
    os.system('clear')
    for filename in os.listdir(osFolder):
        index += [filename]
    try:
        print("選取回寫作業系統 ")
        osGet = enquiries.choose(' Choose clone OS options: ', index)
    except ValueError:
        print(Fore.YELLOW + "未發現作業系統 No OS find " + Fore.RESET, end='')
        print("需先執行OS複製程式...")
        print(" ")
        osGet = "NO_OS"
        input("按任意鍵繼續 Press any key continue...")
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        db['osSave'] = osGet




def cloneCheck():
    with shelve.open('/home/stux/pyPackage/dataBase') as db:
        pn = db['pnSave']
        diskGet = db['diskSave']
        diskShow = db['diskShow']
        osGet = db['osSave']
    os.system('clear')
    print(Fore.YELLOW + "作業系統克隆確認 " + Fore.RESET, end='')
    print(Fore.YELLOW + "OS Clone Setup Check" + Fore.RESET)
    print("PN:", pn)
    print("回寫裝置Clone Disk:", diskShow)
    print("回寫檔案Clone OS:", osGet)
    print("按n鍵結束,其他鍵繼續  ", end='')
    check = input("Back to menu press'n', other key continue: ").lower()
    if check == "n":
        return False
    else:
        return True

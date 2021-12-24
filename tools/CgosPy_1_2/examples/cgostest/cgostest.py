from __future__ import print_function

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2019, congatec AG. All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the BSD 2-clause license which 
accompanies this distribution. 

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the BSD 2-clause license for more details.

The full text of the license may be found at:        
http://opensource.org/licenses/BSD-2-Clause   

--------------------------------------------------------------

Rev 1.0   09-09-2016	LKA		Initial release.
Rev 1.1   13-03-2018	LKA		CGMOD001: Removed ioGetName call because it is not supported.
Rev 1.2   20-02-2019	LKA		Major rework. Added Python3 support (string formatting).
"""

import sys
import argparse
from time import sleep
from getch import getch
import cgos as cg

# Version information 

MAJOR_VERSION_NUMBER = 1
MINOR_VERSION_NUMBER = 0
BUILD_NUMBER = 0

# Flag definitions

flWdogReboot = 0x0001
flagByte = 0

# Display the signon message
print ("\n"
      "congatec CGOS interface test utility ---  Version {:d}.{:d}.{:d} \n"
      "!!!! FOR CONGATEC INTERNAL USAGE ONLY !!!!\n"
      "(C) Copyright 2005-2019 congatec AG\n".format(MAJOR_VERSION_NUMBER, MINOR_VERSION_NUMBER, BUILD_NUMBER))

#---------------------------------------------------------------------------
# Name: HandleGeneric
# Desc: Test generic CGOS functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------
	
def HandleGeneric():
	
	# Board Classes
	CGOS_BOARD_CLASS_CPU = 0x00000001
	CGOS_BOARD_CLASS_VGA = 0x00000002
	CGOS_BOARD_CLASS_IO =  0x00000004
	# Board Open/Count Flags
	CGOS_BOARD_OPEN_FLAGS_DEFAULT = 0
	CGOS_BOARD_OPEN_FLAGS_PRIMARYONLY = 1
																	
	print ("****************************************")
	print ("Testing generic CGOS functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return
	print ("Close board interface.\n")
	if cg.boardClose() == False:
		print ("ERROR: boardClose failed.")
		return
	print ("Total number of available boards: {:d}".format(cg.boardCount(0,0)))
	print ("Number of primary CPU boards: {:d}".format(cg.boardCount(CGOS_BOARD_CLASS_CPU,CGOS_BOARD_OPEN_FLAGS_PRIMARYONLY)))
	print ("Number of primary VGA boards: {:d}".format(cg.boardCount(CGOS_BOARD_CLASS_VGA,CGOS_BOARD_OPEN_FLAGS_PRIMARYONLY)))
	print ("Number of boards with CPU functionality: {:d}".format(cg.boardCount(CGOS_BOARD_CLASS_CPU,0)))
	print ("Number of boards with VGA functionality: {:d}".format(cg.boardCount(CGOS_BOARD_CLASS_VGA,0)))
	boardname = cg.boardGetName()
	if boardname == False:
		print ("ERROR: boardGetName failed.")
		return
	print ("Board name: " + str(boardname))
	print ("\nRe-open board interface.")
	if cg.boardOpenByName(str(boardname)) == False:
		print ("ERROR: boardOpenByName failed.")
		return
	getch()
	boardinfo = cg.boardGetInfo()
	if boardinfo == False: print ("\nERROR: CgosBoardGetInfo failed.\n")
	print ("\nBoard Information Structure\n")
	print ("Size of Structure: {:d}".format(boardinfo['dwSize']))
	print ("Flags: {:X}h".format(boardinfo['dwFlags']))
	print ("Board Name: \"" + str(boardinfo['szBoard']) + "\"")
	print ("Board Sub Name: \"" + str(boardinfo['szBoardSub']) + "\"")
	print ("Manufacturer Name: \"" + str(boardinfo['szManufacturer']) + "\"")
	print ("Manufacturer Code: {:d}".format(boardinfo['dwManufacturer']))
	print ("Manufacturing Date: {:04d}.{:02d}.{:02d}".format(boardinfo['stManufacturingDate']['wYear'], boardinfo['stManufacturingDate']['wMonth'], boardinfo['stManufacturingDate']['wDay']))
	print ("Last Repair Date: {:04d}.{:02d}.{:02d}".format(boardinfo['stLastRepairDate']['wYear'], boardinfo['stLastRepairDate']['wMonth'], boardinfo['stLastRepairDate']['wDay']))
	print ("Repair Counter: {:d}".format(boardinfo['dwRepairCounter']))
	print ("Serial Number: \"" + str(boardinfo['szSerialNumber']) + "\"")
	print ("Part Number: \"" + str(boardinfo['szPartNumber']) + "\"")
	print ("EAN: \"" + str(boardinfo['szEAN']) + "\"")
	print ("Product Revision: {:c}.{:c} ({:04X}h)".format(boardinfo['wProductRevision'] >> 8, boardinfo['wProductRevision'] & 0xff, boardinfo['wProductRevision']))
	print ("System BIOS Revision: {:03x}".format(boardinfo['wSystemBiosRevision']))
	print ("BIOS Interface Revision: {:03x}".format(boardinfo['wBiosInterfaceRevision']))
	print ("BIOS Interface Build Revision: {:03x}".format(boardinfo['wBiosInterfaceBuildRevision']))
	ulBootCount = cg.boardGetBootCounter()
	if ulBootCount == False: print ("ERROR: boardGetBootCounter failed.")
	print ("Boot Counter: {:d}".format(ulBootCount))
	ulRunTime = cg.boardGetRunningTimeMeter()
	if ulRunTime == False: print ("ERROR: boardGetRunningTimeMeter failed.")
	print ("Running Time Meter: {:d}".format(ulRunTime))
	
#---------------------------------------------------------------------------
# Name: HandleVga
# Desc: Test CGOS video functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleVga():
	
	print ("****************************************")
	print ("Testing CGOS video functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return
	ulVgaCount = cg.vgaCount()
	if ulVgaCount != 0: print ("Number of available VGA devices: " + str(ulVgaCount))
	else:
		print ("ERROR: Failed to get number of VGA devices.")
		return
	for ulUnit in range (0, ulVgaCount):
		vgainfo = cg.vgaGetInfo(ulUnit)
		if (cg.vgaGetInfo(ulUnit)) == False: 
			print ("ERROR: Failed to get VGA information for unit %u.") % (ulUnit)
		else:
			print (("\nVGA unit %u information: ") % (ulUnit))
			print ("dwType:            %Xh" % vgainfo['dwType'])
			print ("dwFlags:           %Xh" % vgainfo['dwFlags'])
			print ("dwNativeWidth:     %Xh" % vgainfo['dwNativeWidth'])
			print ("dwNativeHeight:    %Xh" % vgainfo['dwNativeHeight'])
			print ("dwRequestedWidth:  %Xh" % vgainfo['dwRequestedWidth'])
			print ("dwRequestedHeight: %Xh" % vgainfo['dwRequestedHeight'])
			print ("dwRequestedBpp:    %Xh" % vgainfo['dwRequestedBpp'])
			print ("dwMaxBacklight:    %Xh" % vgainfo['dwMaxBacklight'])
			print ("\nPress any key to continue...")
			getch()
	
	# Test backlight functions
	ulBlVal = cg.vgaGetBacklight(0)
	if ulBlVal == False: print ("\nERROR: Failed to get current backlight value.")
	else: print ("\nCurrent backlight value : %u percent" % ulBlVal)
	print ("Set backlight value to 50 percent.")
	if cg.vgaSetBacklight(0,50) == True:
		print ("Press any key to continue...\n")
		getch()
		print ("Set backlight value to 0 percent.")
		if cg.vgaSetBacklight(0,0) == True:
			print ("Press any key  to continue...\n")
			getch()
			print ("Set backlight value to 100 percent.")
			if cg.vgaSetBacklight(0,100) == False:
				print ("ERROR: Failed to set backlight value.\n")
		else: print ("ERROR: Failed to set backlight value.\n")
	else: print ("ERROR: Failed  to set backlight value.\n")
	
	# Test backlight enable functions
	
	print ("\nToggling backlight enable signal.")
	print ("Press any key to continue...\n")
	getch()
	print ("Set backlight enable state to OFF.")
	if cg.vgaSetBacklightEnable(0,0) == True:
		print ("Press any key to continue...\n")
		getch()
		print ("Set backlight enable state to ON.")
		if cg.vgaSetBacklightEnable(0,1) == False:
			print ("ERROR: Failed to set backlight enable state.")
	else:
		print ("Failed to set backlight enable state.")
	ulBlState = cg.vgaGetBacklightEnable(0)
	if ulBlState == False: print ("ERROR: Failed to get backlight enable state.")
	else: print ("Current backlight enable state: %u." % ulBlState)
	
	#Test contrast functions
		
	ulContVal = cg.vgaGetContrast(0)
	if ulContVal == False: print ("\nERROR: Failed to get current contrast value.")
	else: print ("\nCurrent contrast value : %u percent" % ulContVal)
	print ("Set contrast value to 50 percent.")
	if cg.vgaSetContrast(0,50) == True:
		print ("Press any key to continue...\n")
		getch()
		print ("Set contrast value to 0 percent.")
		if cg.vgaSetContrast(0,0) == True:
			print ("Press any key  to continue...\n")
			getch()
			print ("Set contrast value to 100 percent.")
			if cg.vgaSetContrast(0,100) == False:
				print ("ERROR: Failed to set contrast value.\n")
		else: print ("ERROR: Failed to set contrast value.\n")
	else: print ("ERROR: Failed  to set contrast value.\n")

	# Test contrast enable functions
	
	print ("\nToggling contrast enable signal.")
	print ("Press any key to continue...\n")
	getch()
	print ("Set contrast enable state to OFF.")
	if cg.vgaSetContrastEnable(0,0) == True:
		print ("Press any key to continue...\n")
		getch()
		print ("Set contrast enable state to ON.")
		if cg.vgaSetContrastEnable(0,1) == False:
			print ("ERROR: Failed to set contrast enable state.")
	else:
		print ("ERROR: Failed to set contrast enable state.")
	ulContState = cg.vgaGetContrastEnable(0)
	if ulContState == False: print ("ERROR: Failed to get contrast enable state.")
	else: print ("Current contrast enable state: %u." % ulContState)
	
#---------------------------------------------------------------------------
# Name: HandleStorage
# Desc: Test CGOS storage area functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleStorage():

	bufLockPW = "congatec"
														#CGMOD002 v
	print ("****************************************") 
	print ("Testing CGOS storage area functions.")     
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
													    #CGMOD002 ^
	if getch() == 's': return
	
	# Get number of public storage areas
	ulAreaCount = cg.storageAreaCount(0)
	if ulAreaCount != 0: print ("Number of public storage areas: %u.\n" % ulAreaCount)
	else: print ("\nERROR: Failed to get number of public storage areas.\n")
	
	for ulUnit in range (0, ulAreaCount):
		print ("Storage Area %u:" % ulUnit)
		ulAreaType = cg.storageAreaType(ulUnit)
		print ("Type: %08Xh" % ulAreaType)
		ulAreaSize = cg.storageAreaSize(ulUnit)
		print ("Size: %u" % ulAreaSize)
		print ("Blocksize: %u" % cg.storageAreaBlockSize(ulUnit))
		# Test read function
		print ("\nPress any key to read storage area, [s] to skip this test.\n")
		if getch() != 's':
			storageAreaContent = cg.storageAreaRead(ulUnit, 0, ulAreaSize)
			if storageAreaContent != False:
				print (storageAreaContent)
				print ("Storage area successfully read.\n")
			else: 
				print ("ERROR: Failed to read storage area.\n")
		# Test erase function
		print ("Press any key to erase storage area, [s] to skip this test.\n")
		if getch() != 's':
			if cg.storageAreaErase(ulUnit, 0, ulAreaSize) == True: print ("Storage area successfully erased.\n")
			else: print ("ERROR: Failed to erase storage area.\n")
			# Test erase status  function
			ulEraseState = cg.storageAreaEraseStatus(ulUnit, 0, ulAreaSize)
			if ulEraseState != False: print ("Erase state: %Xh\n" % ulEraseState)
			else: print ("ERROR: Failed to get erase state.\n")
		# test write function
		print ("Press any key to write to storage area, [s] to skip this test.\n")
		if getch() != 's':
			pTestBuf = [0x00] * ulAreaSize
			if cg.storageAreaWrite(ulUnit, 0, pTestBuf, len(pTestBuf)) == True: print ("Storage area successfully written.\n")
			else: print ("ERROR: Failed to write to storage area.\n")
		# test lock functions
		print ("Press any key to test lock functions, [s] to skip this test.\n")
		if getch() != 's':
			if cg.storageAreaIsLocked(ulUnit): print ("Storage area is locked.")
			else: print ("Storage area is not locked.")
			if cg.storageAreaLock(ulUnit, str(bufLockPW)) == True: print ("Storage Area successfully locked.")
			else: print ("Failed to lock storage area.")
			if cg.storageAreaUnlock(ulUnit, str(bufLockPW)) == True: print ("Storage area successfully unlocked.")
			else: print ("Failed to unlock storage area.")
			print ("\n")
		print ("Press any key to continue with next area, [e] to skip this test.\n")
		if getch() == 'e': return

#---------------------------------------------------------------------------
# Name: HandleI2C
# Desc: Test CGOS I2C bus functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleI2C():
	
	CGOS_I2C_TYPE_UNKNOWN = 0    	    # I2C bus for unknown or special purposes
	CGOS_I2C_TYPE_PRIMARY = 0x00010000  # primary I2C bus
	CGOS_I2C_TYPE_SMB     = 0x00020000  # system management bus
	CGOS_I2C_TYPE_DDC     = 0x00030000  # I2C bus of the DDC interface
	
	ulPrimaryI2C = 0xFFFFFFFF
	ulDDCI2C = 0xFFFFFFFF
	
	bEEPAddr = 0xA0
	EEP_SIZE = 128
	
	bufEEPOut = [0x00] * EEP_SIZE
	bufEEPIn = [0x00] * EEP_SIZE
	
	print ("****************************************")
	print ("Testing CGOS I2C functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return
	
	ulI2CBusCount = cg.i2cCount()
	if ulI2CBusCount != 0: print ("Number of available I2C busses: %u.\n" % ulI2CBusCount)
	
	# Check type and availability
	for ulUnit in range (0, ulI2CBusCount):
		ulI2CBusType = cg.i2cType(ulUnit)
		if ulI2CBusType == CGOS_I2C_TYPE_PRIMARY: ulPrimaryI2C = ulUnit
		if ulI2CBusType == CGOS_I2C_TYPE_DDC: ulDDCI2C = ulUnit
		if cg.i2cIsAvailable(ulI2CBusType):
			print ("Bus number %u is of type %08Xh and available." % (ulUnit, ulI2CBusType))
		else: print ("ERROR: Failed to get availability state for bus number %u, type %08dh\n" % (ulUnit, ulI2CBusType))
	
    # Perform standard I2C bus read/write tests 
	print ("\nThe next test assumes that an EEPROM with a min. size of 128 bytes is\n"
		"connected to the standard I2C bus. The I2C bus address of the EEPROM is\n"
		"expected to be A0h. The contents of this EEPROM will be filled with a\n"
		"pattern during the test.\n"
		"\nEnter [s] to skip the test, [c] to change the EEPROM base address or any other\n"
		"key to start the test using the above assumptions.\n")
	ch = getch()
	if ch != 's':
		if ch == 'c':
			# Get new parameters
			addr = raw_input("Enter new EEPROM base address (hex.):\n")
			addr = int(addr,16)
			bEEPAddr = addr & 0xFF
		ulMaxFreq = cg.i2cGetMaxFrequency(ulPrimaryI2C)
		if ulMaxFreq != False: print ("Max. frequency of primary I2C bus: %dHz" % ulMaxFreq)
		else: print ("Failed to get max. frequency of primary I2C bus.")
		ulCurrentFreq = cg.i2cGetFrequency(ulPrimaryI2C)
		if ulCurrentFreq != False: print ("Current frequency of primary I2C bus: %dHz" % ulCurrentFreq)
		else: print ("Failed to get current frequency of I2C bus.")
		if cg.i2cSetFrequency(0,ulMaxFreq) == True:
			print ("Set current frequency of primary I2C bus to %dHz." % ulMaxFreq)
		else: print ("Failed to set current frequency of primary I2C bus.")
		ulCurrentFreq = cg.i2cGetFrequency(ulPrimaryI2C)
		if ulCurrentFreq != False: print ("Current frequency of primary I2C bus: %dHz" % ulCurrentFreq)
		else: print ("Failed to get current frequency of I2C bus.")
		print ("\nPress key to continue.\n")
		getch()
		
		bLogWriteSuccess = True
		bLogReadSuccess = True
		bLogReadState = True
		bLogDataError = False

		print ("Fill EEPROM using i2cWriteRegister function.\n"
		"Afterwards read data back using i2cReadRegister and compare with the\n"
		"original write data.\n")
		for usEEPIndex in range (0,EEP_SIZE):
			# Use this to set the out buffer
			bufEEPOut[usEEPIndex] = usEEPIndex
			
			# Write data
			if cg.i2cWriteRegister(ulPrimaryI2C, bEEPAddr, usEEPIndex, bufEEPOut[usEEPIndex]) == False:
				print ("ERROR: Failed to write to EEPROM.")
				bLogWriteSuccess = False
				bLogReadState = False
				break
			# Give 10ms delay to complete EEPROM internal write cycle
			sleep(0.01)
			# Read data back
			bufEEPIn[usEEPIndex] = cg.i2cReadRegister(ulPrimaryI2C, (bEEPAddr | 0x01), usEEPIndex)
			if bufEEPIn[usEEPIndex] != False:
				if bufEEPIn[usEEPIndex] != hex(bufEEPOut[usEEPIndex]):
					print ("ERROR: Read back value does not match.")
					bLogDataError = True
					bLogReadSuccess = False
					break
			else: 
				print ("ERROR: Failed to read from EEPROM.")
				bLogreadSuccess = False
				break
		if bLogWriteSuccess == True:
			print ("Data successfully written to EEPROM.")
			print (bufEEPIn)
		else: print ("Failed to write data - read back skipped.")
		if bLogReadState == True:
			if bLogReadSuccess == True: print ("Data read back and compared successfully.")
			elif bLogDataError == True: print ("ERROR: Read back data does not match write data.")
			else: print ("ERROR: Failed to read data from EEPROM.")
		# Clear buffers
		bufEEPOut = [0x00] * EEP_SIZE
		bufEEPIn = [0x00] * EEP_SIZE
		
		# Now perform same test using standard read/write functions
		print ("\nFill EEPROM using CgosI2CWrite function.\n"
			"Afterwards read data back using CgosI2CRead and compare with the original\n"
			"write data.\n")
		# As EEPROMs always need some time to store the given data internally, we can 
		# not write the whole block. Thus this is only a test whether the CgosI2CWrite
		# function principally works. However, we cannot write the whole block of data
		# with one call, but have to split it up in single writes. First we always set
		# the index, then we send the data to be stored at the given index. */
		
		bLogWriteSuccess = True
		bLogReadSuccess = True
		bLogReadState = True
		bLogDataError = False
		
		for usEEPIndex in range (0x00,EEP_SIZE):
			# Use this to set the in/out buffers
			bufEEPOut[usEEPIndex] = usEEPIndex | 0x80
			# Write data
			if cg.i2cWriteRegister(ulPrimaryI2C, bEEPAddr, usEEPIndex, bufEEPOut[usEEPIndex]) == False:
				print ("ERROR: Failed to write to EEPROM.")
				bLogWriteSuccess == False
				bLogReadState == False
				break
			# Give 10 ms delay to complete EEPROM internal write cycle
			sleep(0.01)
		# Set EEPROM index back to start
		bufEEPIn[0] = 0x00
		if cg.i2cWrite(ulPrimaryI2C, bEEPAddr, bufEEPIn, 1) == False:
			print ("ERROR: Failed to write to EEPROM.")
			bLogWriteSuccess = False
			bLogReadState = False
		sleep(0.1)
		if bLogWriteSuccess == True: print ("Data successfully written to EEPROM.")
		else: print ("Failed to write data - read back skipped.")
		
		# We only read the data back if the write function succeeded
		if bLogReadState == True:
			# Now read the whole EEPROM with one read command
			bufEEPIn = cg.i2cRead(ulPrimaryI2C, bEEPAddr | 0x01, EEP_SIZE)
			if bufEEPIn != False:
				for usEEPIndex in range (0, EEP_SIZE):
					if bufEEPIn[usEEPIndex] != hex(bufEEPOut[usEEPIndex]):
						print ("ERROR: Read back value does not match.")
						bLogDataError = True
						bLogReadSuccess = False
						break
				print (bufEEPIn)
			else: 
				print ("ERROR: Failed to read from EEPROM.")
				bLogReadSuccess = False
		if bLogReadSuccess == True: print ("Data read back and compared successfully.")
		elif bLogDataError == True: print ("ERROR: Read back data does not match write data.")
		else: print ("ERROR: Failed to read data from EEPROM.")
		
		# Perform EPI I2C bus read/write tests
		
		print ("\nThe next test assumes that an EEPROM with a min. size of 128 bytes is\n"
			"connected to the EPI I2C bus. The I2C bus address of the EEPROM is\n"
			"expected to be A0h. The contents of this EEPROM will be filled with a\n"
			"pattern during the test.\n"
			"\nEnter [s] to skip the test, [c] to change the EEPROM base address or any other\n"
			"key to start the test using the above assumptions.\n")

	ch = getch()
	if ch != 's':
		if ch == 'c':
			# Get new parameters
			addr = raw_input("Enter new EEPROM base address (hex.):\n")
			addr = int(addr,16)
			bEEPAddr = addr & 0xFF
		
		bLogWriteSuccess = True
		bLogReadSuccess = True
		bLogReadState = True
		bLogDataError = False

		print ("Fill EEPROM using i2cWriteRegister function.\n"
		"Afterwards read data back using i2cReadRegister and compare with the\n"
		"original write data.\n")
		for usEEPIndex in range (0,EEP_SIZE):
			# Use this to set the out buffer
			bufEEPOut[usEEPIndex] = usEEPIndex
			
			# Write data
			if cg.i2cWriteRegister(ulDDCI2C, bEEPAddr, usEEPIndex, bufEEPOut[usEEPIndex]) == False:
				print ("ERROR: Failed to write to EEPROM.")
				bLogWriteSuccess = False
				bLogReadState = False
				break
			# Give 10ms delay to complete EEPROM internal write cycle
			sleep(0.01)
			# Read data back
			bufEEPIn[usEEPIndex] = cg.i2cReadRegister(ulDDCI2C, (bEEPAddr | 0x01), usEEPIndex)
			if bufEEPIn[usEEPIndex] != False:
				if bufEEPIn[usEEPIndex] != hex(bufEEPOut[usEEPIndex]):
					print ("ERROR: Read back value does not match.")
					bLogDataError = True
					bLogReadSuccess = False
					break
			else: 
				print ("ERROR: Failed to read from EEPROM.")
				bLogreadSuccess = False
				break
		if bLogWriteSuccess == True:
			print ("Data successfully written to EEPROM.")
			print (bufEEPIn)
		else: print ("Failed to write data - read back skipped.")
		if bLogReadState == True:
			if bLogReadSuccess == True: print ("Data read back and compared successfully.")
			elif bLogDataError == True: print ("ERROR: Read back data does not match write data.")
			else: print ("ERROR: Failed to read data from EEPROM.")
		# Clear buffers
		bufEEPOut = [0x00] * EEP_SIZE
		bufEEPIn = [0x00] * EEP_SIZE
		
		# Now perform same test using standard read/write functions
		print ("\nFill EEPROM using CgosI2CWrite function.\n"
			"Afterwards read data back using CgosI2CRead and compare with the original\n"
			"write data.\n")
		# As EEPROMs always need some time to store the given data internally, we can 
		# not write the whole block. Thus this is only a test whether the CgosI2CWrite
		# function principally works. However, we cannot write the whole block of data
		# with one call, but have to split it up in single writes. First we always set
		# the index, then we send the data to be stored at the given index. */
		
		bLogWriteSuccess = True
		bLogReadSuccess = True
		bLogReadState = True
		bLogDataError = False
		
		for usEEPIndex in range (0x00,EEP_SIZE):
			# Use this to set the in/out buffers
			bufEEPOut[usEEPIndex] = usEEPIndex | 0x80
			# Write data
			if cg.i2cWriteRegister(ulDDCI2C, bEEPAddr, usEEPIndex, bufEEPOut[usEEPIndex]) == False:
				print ("ERROR: Failed to write to EEPROM.")
				bLogWriteSuccess == False
				bLogReadState == False
				break
			# Give 10 ms delay to complete EEPROM internal write cycle
			sleep(0.01)
		# Set EEPROM index back to start
		bufEEPIn[0] = 0x00
		if cg.i2cWrite(ulDDCI2C, bEEPAddr, bufEEPIn, 1) == False:
			print ("ERROR: Failed to write to EEPROM.")
			bLogWriteSuccess = False
			bLogReadState = False
		sleep(0.1)
		if bLogWriteSuccess == True: print ("Data successfully written to EEPROM.")
		else: print ("Failed to write data - read back skipped.")
		
		# We only read the data back if the write function succeeded
		if bLogReadState == True:
			# Now read the whole EEPROM with one read command
			bufEEPIn = cg.i2cRead(ulDDCI2C, bEEPAddr | 0x01, EEP_SIZE)
			if bufEEPIn != False:
				for usEEPIndex in range (0, EEP_SIZE):
					if bufEEPIn[usEEPIndex] != hex(bufEEPOut[usEEPIndex]):
						print ("ERROR: Read back value does not match.")
						bLogDataError = True
						bLogReadSuccess = False
						break
				print (bufEEPIn)
			else: 
				print ("ERROR: Failed to read from EEPROM.")
				bLogReadSuccess = False
		if bLogReadSuccess == True: print ("Data read back and compared successfully.")
		elif bLogDataError == True: print ("ERROR: Read back data does not match write data.")
		else: print ("ERROR: Failed to read data from EEPROM." )
	
#---------------------------------------------------------------------------
# Name: HandleWD
# Desc: Test CGOS watchdog functions.
# Inp:  none
# Outp: none
#---------------------------------------------------------------------------

def HandleWD():

	# Watchdog Modes
	CGOS_WDOG_MODE_REBOOT_PC = 0
	CGOS_WDOG_MODE_RESTART_OS = 1
	CGOS_WDOG_MODE_STAGED = 0x80
	# Watchdog OpModes
	CGOS_WDOG_OPMODE_DISABLED = 0
	CGOS_WDOG_OPMODE_ONETIME_TRIG = 1
	CGOS_WDOG_OPMODE_SINGLE_EVENT = 2
	CGOS_WDOG_OPMODE_EVENT_REPEAT = 3
	# Watchdog Events
	CGOS_WDOG_EVENT_INT = 0 # NMI/IRQ
	CGOS_WDOG_EVENT_SCI = 1 # SMI/SCI
	CGOS_WDOG_EVENT_RST = 2 # system reset
	CGOS_WDOG_EVENT_BTN = 3 # power button
	
	print ("****************************************")
	print ("Testing CGOS watchdog functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return
	ulWDCount = cg.wdogCount()
	if ulWDCount != 0: print ("Number of available watchdogs: " + str(ulWDCount))
	else: print ("ERROR: Failed to get number of available watchdogs.")
	ulUnit = 0
	if cg.wdogIsAvailable(ulUnit): print ("Watchdog number %u is available." % ulUnit)
	else: print ("ERROR: Failed to get availablility state of watchdog %u." % ulUnit)
	
	wdinfo = cg.wdogGetInfo(ulUnit)
	if wdinfo != False:
		print ("\nInformation structure for watchdog %u:" % ulUnit)
		print ("Size of Structure: %u" % wdinfo['dwSize'])
		print ("Flags: %Xh" % wdinfo['dwFlags'])
		print ("Min Timeout: %u" % wdinfo['dwMinTimeout'])
		print ("Max Timeout: %u" % wdinfo['dwMaxTimeout'])
		print ("Min Delay: %u" % wdinfo['dwMinDelay'])
		print ("Max Delay %u" % wdinfo['dwMaxDelay'])
		print ("Supported OpModes: %Xh" % wdinfo['dwOpModes'])
		print ("Max Stage Count: %u" % wdinfo['dwMaxStageCount'])
		print ("Supported Events: %Xh" % wdinfo['dwEvents'])
		print ("Type: %08Xh" % wdinfo['dwType'])
	else: print ("ERROR: Failed to get information structure for watchdog %u." % ulUnit)
	print ("\nPress any key to continue...\n")
	getch()
	print("\nThe next test will initialize the watchdog using the simplified\n"
		"CgosWDogSetConfig command. The watchdog will be configured to generate\n"
		"a reset event after a delay of 30secs. and a timeout of 10secs.\n"
		"For reference the watchdog configuration will be read back and displayed.\n"
		"Once started, you can wait for the watchdog to generate the event or\n"
		"enter [t] to trigger and [d] to disable the watchdog.\n")
	print ("\nEnter [s] to skip this test or any other key to start.\n")
	if getch() != 's':
		if cg.wdogSetConfig(ulUnit, 10000, 30000, CGOS_WDOG_MODE_REBOOT_PC):
			print ("Watchdog started.")
			wdgetconfig = cg.wdogGetConfigStruct(ulUnit)
			if wdgetconfig != False:
					print ("Current watchdog %u configuration:" % ulUnit)
					print ("Size of Structure: %u" % wdgetconfig['dwSize'])
					print ("Timeout: %u" % wdgetconfig['dwTimeout'])
					print ("Delay: %u" % wdgetconfig['dwDelay'])
					print ("Mode: %Xh" % wdgetconfig['dwMode'])
					print ("Operating Mode: %Xh" % wdgetconfig['dwOpMode'])
					print ("Stage Count: %u" % wdgetconfig['dwStageCount'])
					print ("Event Stage 1: %08Xh" % wdgetconfig['stStages0']['dwEvent'])
					print ("Timeout Stage 1: %u" % wdgetconfig['stStages0']['dwTimeout'])
					print ("Event Stage 2: %08Xh" % wdgetconfig['stStages1']['dwEvent'])
					print ("Timeout Stage 2: %u" % wdgetconfig['stStages1']['dwTimeout'])
					print ("Event Stage 3: %08Xh" % wdgetconfig['stStages2']['dwEvent'])
					print ("Timeout Stage 3: %u" % wdgetconfig['stStages2']['dwTimeout'])
			else:
				print ("ERROR: Failed to read back watchdog configuration.")
			# trigger the watchdog three times
			for i in range (0,3):
				if (cg.wdogTrigger(ulUnit)) == True: print ("Watchdog triggered.")
				else: print ("ERROR: Failed to trigger watchdog.")
				# sleep 5s
				sleep(5)
			if cg.wdogDisable(ulUnit) == True: print ("Watchdog disabled.")
			else: print ("ERROR: Failed to disable watchdog.")
		else: print ("ERROR: Failed to initialize watchdog.")
		print ("\nPress any key to continue...\n")
		getch()
		print ("\nThe next test will initialize the watchdog using the full featured\n"
			"CgosWDogSetConfigStruct command. The watchdog will be configured to generate\n"
			"a power button event as first stage after a delay of 30secs. and a timeout\n"
			"of 10secs. The second stage after an additional timeout of 20secs will\n"
			"generate a reset event. Operation mode is set to single event.\n"
			"For reference the watchdog configuration will be read back and displayed.\n"
			"Once started, you can wait for the watchdog to generate the event or\n"
			"enter [t] to trigger and [d] to disable the watchdog.\n")
		print ("\nEnter [s] to skip test, any other key to continue.\n")
		if getch() == 's': return
		wdsetconfig = {}
		wdsetconfig['dwMode'] = CGOS_WDOG_MODE_STAGED
		wdsetconfig['dwStageCount'] = 2
		wdsetconfig['dwDelay'] = 30000
		wdsetconfig['dwOpMode'] = CGOS_WDOG_OPMODE_SINGLE_EVENT
		wdsetconfig['stStages0'] = {'dwEvent' : CGOS_WDOG_EVENT_BTN, 'dwTimeout' : 10000}
		wdsetconfig['stStages1'] = {'dwEvent' : CGOS_WDOG_EVENT_RST, 'dwTimeout' : 20000}
		

		if cg.wdogSetConfigStruct(ulUnit, wdsetconfig) == True:
			print ("Watchdog started.\n")
			wdgetconfig = cg.wdogGetConfigStruct(ulUnit)
			if wdgetconfig != False:
					print ("Current watchdog %u configuration:" % ulUnit)
					print ("Size of Structure: %u" % wdgetconfig['dwSize'])
					print ("Timeout: %u" % wdgetconfig['dwTimeout'])
					print ("Delay: %u" % wdgetconfig['dwDelay'])
					print ("Mode: %Xh" % wdgetconfig['dwMode'])
					print ("Operating Mode: %Xh" % wdgetconfig['dwOpMode'])
					print ("Stage Count: %u" % wdgetconfig['dwStageCount'])
					print ("Event Stage 1: %08Xh" % wdgetconfig['stStages0']['dwEvent'])
					print ("Timeout Stage 1: %u" % wdgetconfig['stStages0']['dwTimeout'])
					print ("Event Stage 2: %08Xh" % wdgetconfig['stStages1']['dwEvent'])
					print ("Timeout Stage 2: %u" % wdgetconfig['stStages1']['dwTimeout'])
					print ("Event Stage 3: %08Xh" % wdgetconfig['stStages2']['dwEvent'])
					print ("Timeout Stage 3: %u" % wdgetconfig['stStages2']['dwTimeout'])
			else:
				print ("ERROR: Failed to read back watchdog configuration.")
			while True:
				ch = getch()
				if ch == 't':
					if cg.wdogTrigger(ulUnit) == True: print ("Watchdog triggered.")
					else: print ("ERROR: Failed to  trigger watchdog.")
				if ch == 'd':
					if cg.wdogDisable(ulUnit) == True: print ("Watchdog disabled.")
					else: print ("ERROR: Failed to disable watchdog.")
					break
		else:
			print ("ERROR: Failed to initialize watchdog.")

#---------------------------------------------------------------------------
# Name: HandleMonitor
# Desc: Test CGOS monitor functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleMonitor():
	
	print ("****************************************")
	print ("Testing CGOS monitor functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return
	ulMonCount = cg.temperatureCount()
	print ("Number of temperature monitors: " + str(ulMonCount))
	if ulMonCount != 0:
		for ulUnit in range (0, ulMonCount):
			tempinfo = cg.temperatureGetInfo(ulUnit)
			if tempinfo != False:
				print ("\nTemperature monitor %u information: " % ulUnit)
				print ("Type:        %Xh" % tempinfo['dwType'])
				print ("Flags:       %Xh" % tempinfo['dwFlags'])
				print ("Alarm:       %Xh" % tempinfo['dwAlarm'])
				print ("Resolution:  %d" % tempinfo['dwRes'])
				print ("Max. Value:  %d" % tempinfo['dwMax'])
				print ("Min. Value:  %d" % tempinfo['dwMin'])
				print ("AlarmHigh:   %d" % tempinfo['dwAlarmHi'])
				print ("AlarmLow:    %d" % tempinfo['dwAlarmLo'])
				print ("HystHigh:    %d" % tempinfo['dwHystHi'])
				print ("HystLow:     %d" % tempinfo['dwHystLo'])
				tempcurrent = cg.temperatureGetCurrent(ulUnit)
			else: print ("ERROR: Failed to get info for temperature monitor %u" % ulUnit)
			if tempcurrent != False:
				print ("\nCurrent setting:   " + str(tempcurrent['pdwSetting']))
				print ("Current status:    " + str(tempcurrent['pdwStatus']))
			else: print ("ERROR: Failed to get current temperature monitor %u value." % ulUnit)
			print ("\nPress any key to continue with next monitor.\n")
			getch()

	ulMonCount = cg.voltageCount()
	print ("Number of voltage monitors: " + str(ulMonCount))
	if ulMonCount != 0:
		for ulUnit in range (0, ulMonCount):
			voltageinfo = cg.voltageGetInfo(ulUnit)
			if voltageinfo != False:
				print ("\nVoltage monitor %u information: " % ulUnit)
				print ("Type:          %Xh" % voltageinfo['dwType'])
				print ("Flags:         %Xh" % voltageinfo['dwFlags'])
				print ("Alarm:         %Xh" % voltageinfo['dwAlarm'])
				print ("Resolution:    %d" % voltageinfo['dwRes'])
				print ("Nominal Value: %d" % voltageinfo['dwNom'])
				print ("Max. Value:    %d" % voltageinfo['dwMax'])
				print ("Min. Value:    %d" % voltageinfo['dwMin'])
				print ("AlarmHigh:     %d" % voltageinfo['dwAlarmHi'])
				print ("AlarmLow:      %d" % voltageinfo['dwAlarmLo'])
				print ("HystHigh:      %d" % voltageinfo['dwHystHi'])
				print ("HystLow:       %d" % voltageinfo['dwHystLo'])
				voltagecurrent = cg.voltageGetCurrent(ulUnit)
			else: print ("ERROR: Failed to get info for voltage monitor %u" % ulUnit)
			if voltagecurrent != False:
				print ("\nCurrent setting:   " + str(voltagecurrent['pdwSetting']))
				print ("Current status:    " + str(voltagecurrent['pdwStatus']))
			else: print ("ERROR: Failed to get current voltage monitor %u value." % ulUnit)
			print ("\nPress any key to continue with next monitor.\n")
			getch()
				
	ulMonCount = cg.fanCount()
	print ("Number of fan monitors: " + str(ulMonCount))
	if ulMonCount != 0:
		for ulUnit in range (0, ulMonCount):
			faninfo = cg.fanGetInfo(ulUnit)
			if faninfo != False:
				print ("\Fan monitor %u information: " % ulUnit)
				print ("Type:          %Xh" % faninfo['dwType'])
				print ("Flags:         %Xh" % faninfo['dwFlags'])
				print ("Alarm:         %Xh" % faninfo['dwAlarm'])
				print ("Nominal Value: %d" % faninfo['dwSpeedNom'])
				print ("Max. Value:    %d" % faninfo['dwMax'])
				print ("Min. Value:    %d" % faninfo['dwMin'])
				print ("AlarmHigh:     %d" % faninfo['dwAlarmHi'])
				print ("AlarmLow:      %d" % faninfo['dwAlarmLo'])
				print ("HystHigh:      %d" % faninfo['dwHystHi'])
				print ("HystLow:       %d" % faninfo['dwHystLo'])
				fancurrent = cg.fanGetCurrent(ulUnit)
			else: print ("ERROR: Failed to get info for fan monitor %u" % ulUnit)
			if fancurrent != False:
				print ("\nCurrent setting:   " + str(fancurrent['pdwSetting']))
				print ("Current status:    " + str(fancurrent['pdwStatus']))
			else: print ("ERROR: Failed to get current voltage monitor %u value." % ulUnit)
			print ("\nPress any key to continue with next monitor.\n")
			getch()
			
#---------------------------------------------------------------------------
# Name: HandleGPIO
# Desc: Test CGOS GPIO functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleGPIO():
	
	print ("****************************************")
	print ("Testing CGOS GPIO functions.")
	print ("****************************************")
	print ("Enter [s] to skip test, any other key to continue.\n")
	if getch() == 's': return

    #################
    #    CgosIOCount
    #################
    #Get number of implemented GPIO units. A single GPIO unit can handle up to
    #32 GPIs/GPOs/GPIOs

	print ("\nFunction: CgosIOCount\n"
		"Get number of available GPIO handler units.\n"
		"A single GPIO unit can handle up to 32 GPIs/GPOs/GPIOs.\n")

	ulGpioUnitCount = cg.ioCount()
	print ("Number of available GPIO units: " + str(ulGpioUnitCount))
	
	print ("\nPress any key to continue...\n")
	getch()
	for ulUnit in range(0,ulGpioUnitCount):
		
	######################## 
	#    CgosIOIsAvailable 
	########################
	#Check whether GPIO unit is available.
		print ("Function: ioIsAvailable")
		print ("Check whether GPIO unit with given index can be used.")
		if cg.ioIsAvailable(ulUnit) != True: print ("\nERROR: Failed to get availability state for GPIO unit %u" % ulUnit)
		else: print ("\nGPIO unit %d is available.\n" % ulUnit)

		####################
		# CgosIOGetName
		####################
		# Get name of GPIO unit
		
		'''
		CGMOD001 v
		
		print "Function: ioGetName"
		print "Return name of GPIO unit."
		cUnitName = cg.ioGetName(ulUnit)
		if cUnitName != False: 
			print "GPIO unit %d name: %s" % (ulUnit, cg.ioGetName(ulUnit))
		else: 
			print "ERROR: Failed to get name of GPIO unit." 
		print "\nPress any key to continue...\n"
		getch()
		
		CGMOD001 ^ 
		'''
		
		############################
		# CgosIOGetDirectionCaps
		############################
		# Get direction capabilities of GPIOs handled by a certain GPIO handler.
		print ("\nFunction: ioGetDirectionCaps\n"
			"Return direction capabilities of the pins handled by the selected GPIO unit.\n"
			"A bit set in the input pin field indicates that this bit can handle a GPI.\n"
			"A bit set in the output pin field indicates that this bit can handle a GPO.\n"
			"A bit set in input and output pin field indicates that the corresponding pin's\n"
			"direction can be changed, i.e. this bit handles a GPIO.\n"
			"A bit set only in the input pin field handles a hardwired GPI.\n"
			"A bit set only in the output pin field handles a hardwired GPO.\n"
			"Bit positions set neither in the input nor the output pin fields have\n"
			"no corresponding pin at all.\n")
		pindirections = cg.ioGetDirectionCaps(ulUnit)
		if pindirections != False:
			print ("GPIO unit %d \nInput pins   : %08Xh\nOutput pins  : %08Xh" % (ulUnit, pindirections['pdwInputs'], pindirections['pdwOutputs']))
		else: print ("ERROR: Failed to get direction capabilities ud GPIO unit %d!" % ulUnit)
		print ("\nPress any key to continue...\n")
		getch()
		#########################
		#CgosIOGetDirection
		#########################
		# Get current direction of the GPIO pins. A bit set to 1 in this field indicates that
		# the respective pin is (currently) configured as input, a bit set to 0 indicates that
		# the respective pin is (currently) configured as output, or not implemented
		# (cross check with result of CgosIOGetDirectionCaps which returns the implemented pins).
		print ("\nFunction: ioGetDirection\n"
			"Get current direction of the GPIO pins. A bit set to 1 in this field indicates\n"
			"that the respective pin is configured as input, a bit set to 0 indicates that\n"
			"the respective pin is configured as output, or not implemented\n"
			"(cross check with result of CgosIOGetDirectionCaps).\n")
		ulCurrentPinDirection = cg.ioGetDirection(ulUnit)
		if ulCurrentPinDirection != False:
			print ("\nGPIO unit %d \nCurrent pin direction configuration: %08Xh" % (ulUnit, ulCurrentPinDirection))
		else: print ("ERROR: Failed to get current pin direction configuration of GPIO unit %d!" % ulUnit)
		print ("\nPress any key to continue...\n")
		getch()

		#########################
		# CgosIOSetDirection
		#########################
		# Changing the pin direction configuration is not supported for the COMExpress 
		# GPIO unit as GPI/GPO configuration is fixed by spec./design.
		# Therefore the respective function will fail for COMExpress (added for completeness only).
		print ("Function: ioSetDirection")
		print ("Try to change current pin direction configuration.")
		print ("(Fails if pin direction configuration cannot be changed (e.g. COMExpress))")
		if cg.ioSetDirection(ulUnit, 0xFFFFFFFF) == True:
				print ("\nGPIO unit %d \nPin direction configuration changed." % ulUnit)
		else: print ("\nERROR: Failed to change current pin direction configuration of GPIO unit %d!" % ulUnit)
		print ("\nPress any key to continue...\n")
		getch()
		
		################
		# CgosIORead
		################
		# Read current state of the GPIO pins. A bit set to 1 indicates the respective pin is high,
		# a bit set to 0 indicates the current pin is low or not implemented. Again the mask of implemented 
		# pins derived from the results of CgosIOGetDirectionCaps has to be considered.
		# For pins configured as output, the last state written to this pin is returned
		# (assuming that an output pin always can be set to the desired/requested state).
		
		print ("\nFunction: ioRead\n"
			"Read current state of the GPIO pins. A bit set to 1 indicates the respective\n"
			"pin is high. A bit set to 0 indicates the corresponding pin is low or\n"
			"not implemented. Again the mask of implemented pins derived from the results\n"
			"of CgosIOGetDirectionCaps has to be considered.\n"        
			"For pins configured as output, the last state written to this pin is returned,\n"
			"assuming that an output pin always can be set to the desired/requested state.\n")
		ulGPIOPinState = cg.ioRead(ulUnit)
		if ulGPIOPinState != False:
			print ("GPIO unit %d \nCurrent GPIO pin state: %08Xh" % (ulUnit, ulGPIOPinState))
		else: print ("ERROR: Failed to read pin state of GPIO unit %d!" % ulUnit)
		print ("\nPress any key to continue...\n")
		getch()

		#################
		# CgosIOWrite
		#################
		# Set state of GPIO pins. Of course only the state of pins configured as outputs can be changed.
		# However, the function will gracefully ignore values set for input pins or pins that are not
		# even implemented.
		print ("\nFunction: ioWrite\n"
			"Set state of GPIO pins.\n"
			"Of course only the state of pins configured as outputs can be changed.\n"       
			"However, the function will gracefully ignore values set for input pins or pins\n"
			"that are not even implemented.\n")
		print ("Set all output pins to LOW (ioWrite)")
		if cg.ioWrite(ulUnit, 0x00000000) == False: 
			print ("ERROR: Failed to set output pins of GPIO unit %d!" % ulUnit)
		print ("\nPress any key to continue...\n")
		getch()
		print ("Set all output pins to HIGH (ioWrite)")
		if cg.ioWrite(ulUnit, 0xFFFFFFFF) == False:
			print ("ERROR: Failed to set output pins of GPIO unit %d!" % ulUnit)
		print ("\nPress any key for automatic COMExpress GPIO HW test, [m] for manual test.")
		ch = getch();
		if ch == 'm':
			print ("Set all output pins to HIGH (ioWrite)")
			if cg.ioWrite(ulUnit, 0xFFFFFFFF) == False:
				print ("ERROR: Failed to set output pins of GPIO unit %d!" % ulUnit)
			ulGPIOPinState = cg.ioRead(ulUnit)
			if ulGPIOPinState != False:
				print ("GPIO unit %d \nCurrent GPIO pin state: %08Xh" % (ulUnit, ulGPIOPinState))
			else: print ("ERROR: Failed to read pin state of GPIO unit %d!" % ulUnit)
			print ("\nPress any key to continue...\n")
			getch()
			print ("Set all output pins to LOW (ioWrite)")
			if cg.ioWrite(ulUnit, 0x00000000) == False:
				print ("ERROR: Failed to set output pins of GPIO unit %d!" % ulUnit)
			ulGPIOPinState = cg.ioRead(ulUnit)
			if ulGPIOPinState != False:
				print ("GPIO unit %d \nCurrent GPIO pin state: %08Xh" % (ulUnit, ulGPIOPinState))
			else: print ("ERROR: Failed to read pin state of GPIO unit %d!" % ulUnit)
		else: 
			usGpioHwFail = True
			cg.ioWrite(ulUnit, 0x00000000)
			ulGPIOPinState = cg.ioRead(ulUnit)
			if (ulGPIOPinState & 0x000000FF) == 0x00000000:
				cg.ioWrite(ulUnit, 0x00000010)
				ulGPIOPinState = cg.ioRead(ulUnit)
				if (ulGPIOPinState & 0x000000FF) == 0x00000011:
					cg.ioWrite(ulUnit, 0x00000020)
					ulGPIOPinState = cg.ioRead(ulUnit)
					if (ulGPIOPinState & 0x000000FF) == 0x00000022:
						cg.ioWrite(ulUnit, 0x00000040)
						ulGPIOPinState = cg.ioRead(ulUnit)
						if (ulGPIOPinState & 0x000000FF) == 0x00000044:
							cg.ioWrite(ulUnit, 0x00000080)
							ulGPIOPinState = cg.ioRead(ulUnit)
							if (ulGPIOPinState & 0x000000FF) == 0x00000088:
								cg.ioWrite(ulUnit, 0x000000F0)
								ulGPIOPinState = cg.ioRead(ulUnit)
								if (ulGPIOPinState & 0x000000FF) == 0x000000FF:
									usGpioHwFaile = False
									print ("\nAutomatic COMExpress GPIO hardware test successful!")
			if usGpioHwFail == True: print ("\nERROR: Automatic COMExpress GPIO hardware test failed!")

#---------------------------------------------------------------------------
# Name: HandleTestAll
# Desc: Test all CGOS functions.
# Inp:  none
# Outp: none       
#---------------------------------------------------------------------------

def HandleTestAll():

	HandleGeneric();
	print("\nPress any key to continue...")
	getch();
	HandleVga();
	print("\nPress any key to continue...")
	getch();
	HandleStorage();
	print("\nPress any key to continue...")
	getch();
	HandleI2C();
	print("\nPress any key to continue...")
	getch();
	HandleMonitor();
	print("\nPress any key to continue...")
	getch();
	HandleGPIO();
	print("\nPress any key to continue...")
	getch();
	HandleWD();

# Top level parser
parser = argparse.ArgumentParser(usage = "cgostest [Options] [TEST]")
parser.add_argument('-w', action='store_true', help="force watchdog to reboot system after watchdog test.")

subparsers = parser.add_subparsers()

# subparser for "ALL" command
parser_all = subparsers.add_parser("all", help="Test all functions.")
parser_all.set_defaults(func=HandleTestAll)

# subparser for "GENERIC" command
parser_generic = subparsers.add_parser("generic", help ="Test generic board functions.")
parser_generic.set_defaults(func=HandleGeneric)

# subparser for "VGA" command
parser_vga = subparsers.add_parser("vga", help = "Test generic board functions.")
parser_vga.set_defaults(func=HandleVga)

# subparser for "STORAGE" command
parser_storage = subparsers.add_parser("storage", help ="Test storage area functions.")
parser_storage.set_defaults(func=HandleStorage)

# subparser for "I2C" command
parser_i2c = subparsers.add_parser("i2c", help ="Test I2C bus functions.")
parser_i2c.set_defaults(func=HandleI2C)

# subparser for "WD" command
parser_wd = subparsers.add_parser("wd", help ="Test watchdog functions.")
parser_wd.set_defaults(func=HandleWD)

# subparser for "MONITOR" command
parser_monitor = subparsers.add_parser("monitor", help ="Test monitor functions.")
parser_monitor.set_defaults(func=HandleMonitor)

# subparser for "GPIO" command
parser_gpio = subparsers.add_parser("gpio", help ="Test GPIO functions.")
parser_gpio.set_defaults(func=HandleGPIO)

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
    
args=parser.parse_args()

if cg.openif() == True:
	args.func()
	cg.boardGetInfo()
	cg.closeif()

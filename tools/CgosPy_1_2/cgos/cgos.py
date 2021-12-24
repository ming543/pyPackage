from __future__ import print_function #CGMOD003

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018, congatec AG. All rights reserved.

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
Rev 1.1   13-03-2018	LKA		MOD001: Removed ioGetName because it is not supported.
                                MOD002: Changed data type in Changed data type in array_type_write and array_type_read 
                                          from unsigned int (ctypes.c_uint) to unsigned char (ctypes.c_ubyte)
Rev 1.2	  20-03-2019	LKA		MOD003: Added Python3 support
"""

""" 

ctypes wrapper for accessing the CGOS API shared object / DLL

"""


import ctypes
from sys import platform

# Determine the OS and load the shared object / DLL accordingly:
if platform == "linux" or platform == "linux2":
	# Linux -> load the shared object
	_cgos = ctypes.CDLL("libcgos.so")
elif platform == "win32":
    # Windows -> load the DLL
    _cgos = ctypes.WinDLL("cgos.dll")
else:
    #OS not recognized -> display error message and exit
  print ("ERROR: Could not determine operating system.") #MOD003
  sys.exit(1)

hCgos = ctypes.c_uint(0)

	####################################
	##### FUNCTION GROUP CGOSBOARD #####
	####################################

# ulong CgosLibGetVersion(void)
def libGetVersion():
	_cgos.CgosLibGetVersion.restype = ctypes.c_ulong
	return _cgos.CgosLibGetVersion()
	
# bool CgosLibInitialize(void)
def libInitialize():
	_cgos.CgosLibInitialize.restype = ctypes.c_bool
	return _cgos.CgosLibInitialize()

# bool CgosLibUninitialize(void)
def libUninitialize():
	_cgos.CgosLibUninitialize.restype = ctypes.c_bool
	return _cgos.CgosLibUninitialize()

# bool CgosLibIsAvailable(void)
def libIsAvailable():
	_cgos.CgosLibIsAvailable.restype = ctypes.c_bool
	return _cgos.CgosLibIsAvailable()

# bool CgosLibInstall(unsigned int install)
def libInstall(install):
	_cgos.CgosLibInstall.argytpes = (ctypes.c_uint)
	_cgos.CgosLibInstall.restype = ctypes.c_bool
	return _cgos.CgosLibInstall(install)

# ulong CgosLibGetDrvVersion(void)
def libGetDrvVersion():
	_cgos.CgosLibGetDrvVersion.restype = ctypes.c_ulong
	return _cgos.CgosLibGetDrvVersion()

# ulong CgosLibGetLastError(void)
def libGetLastError():
	_cgos.CgosLibGetLastError.restype = ctypes.c_ulong
	return _cgos.CgosLibGetLastError()

# bool CgosLibSetLastErrorAddress(unsigned long *pErrNo)
def libSetLastErrorAddress(pErrNo):
#	val = ctypes.c_ulong(pErrNo)
#	_cgos.CgosLibSetLastErrorAddress.argtypes = (ctypes.POINTER(ctypes.c_ulong))
#	_cgos.CgosLibSetLastErrorAddress.restype = ctypes.c_bool
#	return _cgos.CgosLibSetLastErrorAddress(byref(val))
	return False;

# ulong CgosBoardCount(unsigned long dwClass,unsigned long dwFlags)
def boardCount(dwClass, dwFlags):
	_cgos.CgosBoardCount.argtypes = (ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosBoardCount.restype = ctypes.c_ulong
	return _cgos.CgosBoardCount(dwClass, dwFlags)

# bool CgosBoardOpen(unsigned long dwClass, unsigned long dwNum, unsigned long dwFlags, HCGOS *phCgos)
def boardOpen(dwClass, dwNum, dwFlags):
	_cgos.CgosBoardOpen.argtypes = (ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint))
	_cgos.CgosBoardOpen.restype = ctypes.c_bool
	return _cgos.CgosBoardOpen(dwClass, dwNum, dwFlags, ctypes.byref(hCgos))

# bool CgosBoardOpenByName(const char *pszName, HCGOS *phCgos)
def boardOpenByName(pszName):
	_cgos.CgosBoardOpenByNameA.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint))
	_cgos.CgosBoardOpenByNameA.retype = ctypes.c_bool
	pszName = str.encode(pszName) #MOD003
	name = ctypes.create_string_buffer(pszName)
	retval = _cgos.CgosBoardOpenByNameA(name, ctypes.byref(hCgos))
	if retval == 1: return True
	else: return False

# bool CgosBoardClose(HCGOS hCgos)
def boardClose():
	_cgos.CgosBoardClose.argtype = ctypes.c_uint
	_cgos.CgosBoardClose.restype = ctypes.c_bool
	return _cgos.CgosBoardClose(hCgos)

# bool CgosBoardGetName(HCGOS hCgos, const char *pszName, unsigned long dwSize)
def boardGetName():
	_cgos.CgosBoardGetNameA.argtypes = (ctypes.c_uint, ctypes.c_char_p, ctypes.c_ulong)
	_cgos.CgosBoardGetNameA.restype = ctypes.c_bool
	dwSize = ctypes.c_ulong(16)
	pszName = ctypes.create_string_buffer(dwSize.value)
	if _cgos.CgosBoardGetNameA(hCgos, pszName, dwSize) == True: return pszName.value.decode() #MOD003
	else: return False

# bool CgosBoardGetInfo(HCGOS hCgos, CGOSBOARDINFO *pBoardInfo)
def boardGetInfo():
	CGOS_BOARD_MAX_LEN_ID_STRING = 7
	CGOS_BOARD_MAX_SIZE_ID_STRING = 16
	CGOS_BOARD_MAX_LEN_SERIAL_STRING = 12
	CGOS_BOARD_MAX_SIZE_SERIAL_STRING = 16
	CGOS_BOARD_MAX_LEN_PART_STRING = 16
	CGOS_BOARD_MAX_SIZE_PART_STRING = 20
	CGOS_BOARD_MAX_LEN_EAN_STRING = 13
	CGOS_BOARD_MAX_SIZE_EAN_STRING = 20   
		
	class CGOSTIME(ctypes.Structure):
		_fields_ = [
			('wYear', ctypes.c_ushort),
			('wMonth', ctypes.c_ushort),
			('wDayOfWeek', ctypes.c_ushort),
			('wDay', ctypes.c_ushort),
			('wHour', ctypes.c_ushort),
			('wMinute', ctypes.c_ushort),
			('wSecond', ctypes.c_ushort),
			('wMilliseconds', ctypes.c_ushort),
		]

	class CGOSBOARDINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('szReserved', ctypes.c_char * CGOS_BOARD_MAX_SIZE_ID_STRING),
			('szBoard', ctypes.c_char * CGOS_BOARD_MAX_SIZE_ID_STRING),
			('szBoardSub', ctypes.c_char * CGOS_BOARD_MAX_SIZE_ID_STRING),
			('szManufacturer', ctypes.c_char * CGOS_BOARD_MAX_SIZE_ID_STRING),	
			('stManufacturingDate', CGOSTIME),
			('stLastRepairDate', CGOSTIME),
			('szSerialNumber', ctypes.c_char * CGOS_BOARD_MAX_SIZE_SERIAL_STRING),
			('wProductRevision', ctypes.c_ushort),
			('wSystemBiosRevision', ctypes.c_ushort),
			('wBiosInterfaceRevision', ctypes.c_ushort),
			('wBiosInterfaceBuildRevision', ctypes.c_ushort),
			('dwClasses', ctypes.c_uint),
			('dwPrimaryClasses', ctypes.c_uint),
			('dwRepairCounter', ctypes.c_uint),
			('szPartNumber', ctypes.c_char * CGOS_BOARD_MAX_SIZE_PART_STRING),
			('szEAN', ctypes.c_char * CGOS_BOARD_MAX_SIZE_EAN_STRING),
			('dwManufacturer', ctypes.c_uint),
		]
	      
	cgosboardinfo = CGOSBOARDINFO(0)
	cgostime = CGOSTIME(0)
	cgosboardinfo.dwSize = (ctypes.sizeof(ctypes.c_uint32) * 2) + (ctypes.sizeof(ctypes.c_char) * CGOS_BOARD_MAX_SIZE_ID_STRING * 4)
	cgosboardinfo.dwSize += ((ctypes.sizeof(ctypes.c_ushort)*len(cgostime._fields_)*2) + (ctypes.sizeof(ctypes.c_char) * CGOS_BOARD_MAX_SIZE_ID_STRING))
	cgosboardinfo.dwSize += ((ctypes.sizeof(ctypes.c_ushort) * 4) + (ctypes.sizeof(ctypes.c_uint) * 4))
	cgosboardinfo.dwSize += ((ctypes.sizeof(ctypes.c_char) * CGOS_BOARD_MAX_SIZE_PART_STRING) + (ctypes.sizeof(ctypes.c_char) * CGOS_BOARD_MAX_SIZE_EAN_STRING))
	_cgos.CgosBoardGetInfoA.argtypes = (ctypes.c_uint, ctypes.c_voidp)
	_cgos.CgosBoardGetInfoA.restype = ctypes.c_bool
	if (_cgos.CgosBoardGetInfoA(hCgos, ctypes.addressof(cgosboardinfo))) == True:
		results = {}
		manufacturingdate = {}
		lastrepairdate = {}
		for field in cgosboardinfo._fields_: results[field[0]] = getattr(cgosboardinfo, field[0])
		for field in cgosboardinfo.stManufacturingDate._fields_: manufacturingdate[field[0]] =  getattr(cgosboardinfo.stManufacturingDate, field[0])
		for field in cgosboardinfo.stLastRepairDate._fields_: lastrepairdate[field[0]] =  getattr(cgosboardinfo.stLastRepairDate, field[0])
		results['stManufacturingDate'] = manufacturingdate
		results['stLastRepairDate'] = lastrepairdate
		#MOD003 v
		results['szBoard'] = results['szBoard'].decode()
		results['szBoardSub'] = results['szBoardSub'].decode()
		results['szManufacturer'] = results['szManufacturer'].decode()
		results['szSerialNumber'] = results['szSerialNumber'].decode()
		results['szPartNumber'] = results['szPartNumber'].decode()
		results['szEAN'] = results['szEAN'].decode()
		#MOD003 ^
		return results
	else: return False

# bool CgosBoardGetBootcounter(HCGOS hCgos, unsigned long *pdwCount)
def boardGetBootCounter():
	_cgos.CgosBoardGetBootCounter.argtypes = (ctypes.c_uint, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosBoardGetBootCounter.restype = ctypes.c_bool
	pdwCount = ctypes.c_ulong(0)
	if (_cgos.CgosBoardGetBootCounter(hCgos, pdwCount)) == True: return pdwCount.value
	else: return False

# bool CgosBoardGetRunningTimeMeter(HCGOS hCgos, unsigned long *pdwCount)
def boardGetRunningTimeMeter():
	_cgos.CgosBoardGetRunningTimeMeter.argtypes = (ctypes.c_uint, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosBoardGetRunningTimeMeter.restype = ctypes.c_bool
	pdwCount = ctypes.c_ulong(0)
	if(_cgos.CgosBoardGetRunningTimeMeter(hCgos, pdwCount)) == True: return pdwCount.value
	else: return False

	##################################
	##### FUNCTION GROUP CGOSVGA #####
	##################################

# ulong CgosVgaCount(HCGOS hCgos)
def vgaCount():
	_cgos.CgosVgaCount.argtype = ctypes.c_uint
	_cgos.CgosVgaCount.restype = ctypes.c_ulong
	return _cgos.CgosVgaCount(hCgos)

# bool CgosVgaGetBacklight(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting)
def vgaGetBacklight(dwUnit):
	_cgos.CgosVgaGetBacklight.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosVgaGetBacklight.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	if (_cgos.CgosVgaGetBacklight(hCgos, dwUnit, pdwSetting)) == True: return pdwSetting.value
	else: return False

# bool CgosVgaSetBacklight(HCGOS hCgos, unsigned long dwUnit, unsigned long dwSetting)
def vgaSetBacklight(dwUnit, dwSetting):
	_cgos.CgosVgaSetBacklight.argytpes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosVgaSetBacklight.restype = ctypes.c_bool
	if dwSetting > 100: return False
	return _cgos.CgosVgaSetBacklight(hCgos, dwUnit, dwSetting)

# bool CgosVgaGetBacklightEnable(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting)
def vgaGetBacklightEnable(dwUnit):
	_cgos.CgosVgaGetBacklightEnable.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosVgaGetBacklightEnable.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	if (_cgos.CgosVgaGetBacklightEnable(hCgos, dwUnit, pdwSetting)) == True: return pdwSetting.value
	else: return False

# bool CgosVgaSetBacklightEnable(HCGOS hCgos, unsigned long dwUnit, unsigned long dwSetting)
def vgaSetBacklightEnable(dwUnit, dwSetting):
	_cgos.CgosVgaSetBacklightEnable.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosVgaSetBacklightEnable.restype = ctypes.c_bool
	return _cgos.CgosVgaSetBacklightEnable(hCgos,dwUnit,dwSetting)

# bool CgosVgaGetInfo(HCGOS hCgos, unsigned long dwUnit, CGOSVGAINFO *pInfo)
def vgaGetInfo(dwUnit):	
	class CGOSVGAINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwType', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('dwNativeWidth', ctypes.c_uint32),
			('dwNativeHeight', ctypes.c_uint32),
			('dwRequestedWidth', ctypes.c_uint32),
			('dwRequestedHeight', ctypes.c_uint32),
			('dwRequestedBpp', ctypes.c_uint32),
			('dwMaxBacklight', ctypes.c_uint32),
			('dwMaxContrast', ctypes.c_uint32),
		]
		
	cgosvgainfo = CGOSVGAINFO(0)
	cgosvgainfo.dwSize = len((cgosvgainfo._fields_) * ctypes.sizeof(ctypes.c_uint32))
	_cgos.CgosVgaGetInfo.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosVgaGetInfo.restype = ctypes.c_bool
	if (_cgos.CgosVgaGetInfo(hCgos, dwUnit, ctypes.addressof(cgosvgainfo))) == True:
		results = {}
		for field in cgosvgainfo._fields_: results[field[0]] = getattr(cgosvgainfo, field[0])
		return results
	else: return False

# cgosret_bool CgosVgaGetContrast(HCGOS hCgos, unsigned int dwUnit, unsigned int *pdwSetting);
def vgaGetContrast(dwUnit):
	_cgos.CgosVgaGetContrast.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint))
	_cgos.CgosVgaGetContrast.restype = ctypes.c_bool
	pdwSetting = ctypes.c_uint(0)
	if _cgos.CgosVgaGetContrast(hCgos, dwUnit, ctypes.byref(pdwSetting)) == True: return pdwSetting.value
	else: return False

# cgosret_bool CgosVgaSetContrast(HCGOS hCgos, unsigned int dwUnit, unsigned int dwSetting);
def vgaSetContrast (dwUnit, dwSetting):
	_cgos.CgosVgaSetContrast.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
	_cgos.CgosVgaSetContrast.restype = ctypes.c_bool
	return _cgos.CgosVgaSetContrast(hCgos, dwUnit, dwSetting)

# cgosret_bool CgosVgaGetContrastEnable(HCGOS hCgos, unsigned int dwUnit, unsigned int *pdwSetting);
def vgaGetContrastEnable(dwUnit):
	_cgos.CgosVgaGetContrastEnable.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint))
	_cgos.CgosVgaGetContrastEnable.restype = ctypes.c_bool
	pdwSetting = ctypes.c_uint(0)
	if _cgos.CgosVgaGetContrastEnable(hCgos, dwUnit, ctypes.byref(pdwSetting)) == True: return pdwSetting.value
	else: return False

# cgosret_bool CgosVgaSetContrastEnable(HCGOS hCgos, unsigned int dwUnit, unsigned int dwSetting);
def vgaSetContrastEnable (dwUnit, dwSetting):
	_cgos.CgosVgaSetContrastEnable.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
	_cgos.CgosVgaSetContrastEnable.restype = ctypes.c_bool
	return _cgos.CgosVgaSetContrastEnable(hCgos, dwUnit, dwSetting)

	######################################
	##### FUNCTION GROUP CGOSSTORAGE #####
	######################################

# ulong CgosStorageAreaCount(HCGOS hCgos, unsigned long dwUnit)
def storageAreaCount(dwUnit):
	_cgos.CgosStorageAreaCount.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosStorageAreaCount.restype = ctypes.c_ulong
	return _cgos.CgosStorageAreaCount(hCgos, dwUnit)

# ulong CgosStorageAreaType(HCGOS hCgos, unsigned long dwUnit)
def storageAreaType(dwUnit):
	_cgos.CgosStorageAreaType.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosStorageAreaType.restype = ctypes.c_ulong
	return _cgos.CgosStorageAreaType(hCgos, dwUnit)

# ulong CgosStorageAreaSize(HCGOS hCgos, unsigned long dwUnit)
def storageAreaSize (dwUnit):
	_cgos.CgosStorageAreaSize.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosStorageAreaSize.restype = ctypes.c_ulong
	return _cgos.CgosStorageAreaSize(hCgos, dwUnit)

# ulong CgosStorageAreaBlockSize(HCGOS hCgos, unsigned long dwUnit)
def storageAreaBlockSize(dwUnit):
	_cgos.CgosStorageAreaBlockSize.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosStorageAreaBlockSize.restype = ctypes.c_ulong
	return _cgos.CgosStorageAreaBlockSize(hCgos,dwUnit)

# bool CgosStorageAreaRead(HCGOS hCgos, unsigned long dwUnit, unsigned long dwOffset, unsigned char *pBytes, unsigned long dwLen)
def storageAreaRead(dwUnit, dwOffset, dwLen):
	array_type = ctypes.c_ubyte * dwLen
	read_buffer = array_type()
	_cgos.CgosStorageAreaRead.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(array_type), ctypes.c_ulong)
	_cgos.CgosStorageAreaRead.restype = ctypes.c_bool
	if (_cgos.CgosStorageAreaRead(hCgos, dwUnit, dwOffset, read_buffer, dwLen)) == True: 
		ret_list = []
		for i in read_buffer: ret_list.append(hex(i))
		return ret_list
	else:  return False

# bool CgosStorageAreaWrite(HCGOS hCgos, unsigned long dwUnit, unsigned long dwOffset, unsigned char *pBytes, unsigned long dwLen)
def storageAreaWrite(dwUnit, dwOffset, pBytes, dwLen):
	array_type = ctypes.c_ubyte * dwLen
	write_buffer = array_type()
	for i in range (0,dwLen): write_buffer[i] = pBytes[i]
	_cgos.CgosStorageAreaWrite.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(array_type), ctypes.c_ulong)
	_cgos.CgosStorageAreaWrite.restype = ctypes.c_bool
	return (_cgos.CgosStorageAreaWrite(hCgos, dwUnit, dwOffset, write_buffer, dwLen))

# bool CgosStorageAreaErase(HCGOS hCgos, unsigned long dwUnit, unsigned long dwOffset, unsigned long dwLen)
def storageAreaErase(dwUnit, dwOffset, dwLen):
	_cgos.CgosStorageAreaErase.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosStorageAreaErase.restype = ctypes.c_bool
	return _cgos.CgosStorageAreaErase(hCgos, dwUnit, dwOffset, dwLen)

# bool CgosStorageAreaEraseStatus(HCGOS hCgos, unsigned long dwUnit, unsigned long dwOffset, unsigned long dwLen, unsigned long *lpStatus)
def storageAreaEraseStatus(dwUnit, dwOffset, dwLen):
	_cgos.CgosStorageAreaEraseStatus.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosStorageAreaEraseStatus.restype = ctypes.c_bool
	lpStatus = ctypes.c_ulong(0)
	if( _cgos.CgosStorageAreaEraseStatus(hCgos, dwUnit, dwOffset, dwLen, ctypes.byref(lpStatus))) == True: return lpStatus.value
	else: return False

# bool CgosStorageAreaLock(HCGOS hCgos, unsigned long dwUnit, unsigned long dwFlags, unsigned char *pBytes, unsigned long dwLen)
def storageAreaLock(dwUnit, pBytes):
	#MOD003_cgos.CgosStorageAreaLock.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p, ctypes.c_ulong)
	_cgos.CgosStorageAreaLock.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_wchar_p, ctypes.c_ulong) #MOD003
	_cgos.CgosStorageAreaLock.restype = ctypes.c_bool
	#MOD003secret_string = ctypes.create_string_buffer(pBytes)
	secret_string = ctypes.create_unicode_buffer(pBytes)
	dwLen = len(pBytes)
	#dwFlags is reserved for future use -> set to 0
	return _cgos.CgosStorageAreaLock(hCgos, dwUnit, 0, secret_string, dwLen)

# bool CgosStorageAreaUnlock(HCGOS hCgos, unsigned long dwUnit, unsigned long dwFlags, unsigned char *pBytes, unsigned long dwLen)
def storageAreaUnlock(dwUnit, pBytes):
	#MOD003 _cgos.CgosStorageAreaUnlock.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p, ctypes.c_ulong)
	_cgos.CgosStorageAreaUnlock.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_wchar_p, ctypes.c_ulong) #MOD003
	_cgos.CgosStorageAreaUnlock.restype = ctypes.c_bool
	#MOD003secret_string = ctypes.create_string_buffer(pBytes)
	secret_string = ctypes.create_unicode_buffer(pBytes) #MOD003
	dwLen = len(pBytes)
	#dwFlags is reserved for future use -> set to 0
	return _cgos.CgosStorageAreaUnlock(hCgos, dwUnit, 0, secret_string, dwLen)

# bool CgosStorageAreaIsLocked(HCGOS hCgos, unsigned long dwUnit, unsigned long dwFlags)
def storageAreaIsLocked(dwUnit):
	_cgos.CgosStorageAreaIsLocked.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosStorageAreaIsLocked.restype = ctypes.c_bool
	#dwFlags is reserved for future use -> set to 0
	return _cgos.CgosStorageAreaIsLocked(hCgos, dwUnit, 0)

	##################################
	#####   FUNCTION GROUP I2C   #####
	##################################

# ulong CgosI2CCount(HCGOS hCgos)
def i2cCount():
	_cgos.CgosI2CCount.argtype = ctypes.c_uint
	_cgos.CgosI2CCount.restype = ctypes.c_ulong
	return _cgos.CgosI2CCount(hCgos)

# ulong CgosI2CType(HCGOS hCgos, unsigned long dwUnit)
def i2cType(dwUnit):
	_cgos.CgosI2CType.argtypes = (ctypes.c_uint, ctypes.c_uint)
	_cgos.CgosI2CType.restype = ctypes.c_uint
	return _cgos.CgosI2CType(hCgos, dwUnit)

# bool CgosI2CIsAvailable(HCGOS hCgos, unsigned long dwUnit)
def i2cIsAvailable(dwUnit):
	_cgos.CgosI2CIsAvailable.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosI2CIsAvailable.restype = ctypes.c_bool
	return _cgos.CgosI2CIsAvailable(hCgos, dwUnit)

# bool CgosI2CRead(HCGOS hCgos, unsigned long dwUnit, unsigned char bAddr, unsigned char *pBytes, unsigned long dwLen)
def i2cRead(dwUnit, bAddr, dwLen):
	array_type = ctypes.c_ubyte * dwLen
	read_buffer = array_type()
	_cgos.CgosI2CRead.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ubyte, ctypes.POINTER(array_type), ctypes.c_ulong)
	_cgos.CgosI2CRead.restype = ctypes.c_bool
	if (_cgos.CgosI2CRead(hCgos, dwUnit, bAddr, read_buffer, dwLen)) == True:
		ret_list = []
		for i in read_buffer: ret_list.append(hex(i)) 
		return ret_list
	else: return False

# bool CgosI2CWrite(HCGOS hCgos, unsigned long dwUnit, unsigned char bAddr, unsigned char *pBytes, unsigned long dwLen)
def i2cWrite(dwUnit, bAddr, pBytes, dwLen):
	array_type = ctypes.c_ubyte * dwLen
	write_buffer = array_type()
	for i in range (0,dwLen): write_buffer[i] = pBytes[i]
	_cgos.CgosI2CWrite.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ubyte, array_type, ctypes.c_ulong)
	_cgos.CgosI2CWrite.restype = ctypes.c_bool
	return _cgos.CgosI2CWrite(hCgos, dwUnit, bAddr, write_buffer, dwLen)

# bool CgosI2CReadRegister(HCGOS hCgos, unsigned long dwUnit, unsigned char bAddr, unsigned short wReg, unsigned char *pDataByte)
def i2cReadRegister(dwUnit, bAddr, wReg):
	array_type = ctypes.c_ubyte * 1
	read_buffer = array_type()
	_cgos.CgosI2CReadRegister.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ubyte, ctypes.c_ubyte, array_type)
	_cgos.CgosI2CReadRegister.restype = ctypes.c_bool
	if (_cgos.CgosI2CReadRegister(hCgos, dwUnit, bAddr, wReg, read_buffer)) == True: return hex(read_buffer[0])
	else: return False

# bool CgosI2CWriteRegister(HCGOS hCgos, unsigned long dwUnit, unsigned char bAddr, unsigned short wReg, unsigned char bData)
def i2cWriteRegister(dwUnit, bAddr, wReg, bData):
	array_type = ctypes.c_ubyte * 2
	writebuffer = array_type()
	writebuffer[0] = bData
	_cgos.CgosI2CWriteRegister.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ubyte, ctypes.c_ushort, ctypes.c_ubyte)
	_cgos.CgosI2CWriteRegister.restype = ctypes.c_bool
	return _cgos.CgosI2CWriteRegister(hCgos,dwUnit,bAddr,wReg,writebuffer[0])

# bool CgosI2CWriteReadCombined(HCGOS hCgos, unsigned long dwUnit, unsigned char bAddr, unsigned char *pBytesWrite, unsigned long dwLenWrite, unsigned char *pBytesRead, unsigned long dwLenRead)
def i2cWriteReadCombined(dwUnit, bAddr, pBytesWrite, dwLenWrite, dwLenRead):
	#MOD002 v
	#array_type_write = ctypes.c_uint * dwLenWrite
	#array_type_read = ctypes.c_uint * dwLenRead
	array_type_write = ctypes.c_ubyte * dwLenWrite
	array_type_read = ctypes.c_ubyte * dwLenRead
	#MOD002 ^
	write_buffer = array_type_write()
	read_buffer = array_type_read()
	for i in range (0,dwLenWrite): write_buffer[i] = pBytesWrite[i]
	_cgos.CgosI2CWriteReadCombined.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ubyte, array_type_write, ctypes.c_ulong, ctypes.POINTER(array_type_read), ctypes.c_ulong)
	_cgos.CgosI2CWriteReadCombined.restype = ctypes.c_bool
	if (_cgos.CgosI2CWriteReadCombined(hCgos, dwUnit, bAddr, write_buffer, dwLenWrite, read_buffer, dwLenRead)) == True: 
		ret_list = []
		for i in read_buffer: ret_list.append(hex(i)) 
		return ret_list
	else: return False

# bool CgosI2CGetMaxFrequency(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting)
def i2cGetMaxFrequency(dwUnit):
	_cgos.CgosI2CGetMaxFrequency.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosI2CGetMaxFrequency.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	if _cgos.CgosI2CGetMaxFrequency(hCgos, dwUnit,  pdwSetting) == True: return pdwSetting.value
	else: return False

# bool CgosI2CGetFrequency(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting)
def i2cGetFrequency(dwUnit):
	_cgos.CgosI2CGetFrequency.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosI2CGetFrequency.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	if _cgos.CgosI2CGetFrequency(hCgos, dwUnit, pdwSetting) == True: return pdwSetting.value
	else: return False
# bool CgosI2CSetFrequency(HCGOS hCgos, unsigned long dwUnit, unsigned long pdwSetting)
def i2cSetFrequency(dwUnit, pdwSetting):
	_cgos.CgosI2CSetFrequency.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosI2CSetFrequency.restype = ctypes.c_bool
	return _cgos.CgosI2CSetFrequency(hCgos, dwUnit, pdwSetting)

	#################################
	#####   FUNCTION GROUP IO   #####
	#################################

# ulong CgosIOCount(HCGOS hCgos)
def ioCount():
	_cgos.CgosIOCount.argtype = ctypes.c_uint
	_cgos.CgosIOCount.restype = ctypes.c_ulong
	return _cgos.CgosIOCount(hCgos)

# bool CgosIOIsAvailable(HCGOS hCgos, unsigned long dwUnit)
def ioIsAvailable(dwUnit):
	_cgos.CgosIOIsAvailable.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosIOIsAvailable.restype = ctypes.c_bool
	return _cgos.CgosIOIsAvailable(hCgos, dwUnit)
	
# bool CgosIORead(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwData)
def ioRead(dwUnit):
	_cgos.CgosIORead.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosIORead.restype = ctypes.c_bool
	pdwData = ctypes.c_ulong(0)
	if _cgos.CgosIORead(hCgos, dwUnit, ctypes.byref(pdwData)) == True: return pdwData.value
	else: return False

# bool CgosIOWrite(HCGOS hCgos, unsigned long dwUnit, unsigned long dwData)
def ioWrite(dwUnit, dwData):
	_cgos.CgosIOWrite.argtypes =(ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosIOWrite.restype = ctypes.c_bool
	return _cgos.CgosIOWrite(hCgos, dwUnit, dwData)

# bool CgosIOGetDirectionCaps(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwInputs, unsigned long *pdwOutputs)
def ioGetDirectionCaps(dwUnit):
	_cgos.CgosIOGetDirectionCaps.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosIOGetDirectionCaps.restype = ctypes.c_bool
	pdwInputs = ctypes.c_ulong(0)
	pdwOutputs = ctypes.c_ulong(0)
	if _cgos.CgosIOGetDirectionCaps(hCgos, dwUnit, pdwInputs, pdwOutputs) == True:
		results = {'pdwInputs': pdwInputs.value, 'pdwOutputs' : pdwOutputs.value}
		return results
	else: return False

# bool CgosIOGetDirection(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwData)
def ioGetDirection(dwUnit):
	_cgos.CgosIOGetDirection.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosIOGetDirection.restype = ctypes.c_bool
	pdwData = ctypes.c_ulong(0)
	if _cgos.CgosIOGetDirection(hCgos, dwUnit, pdwData) == True: return pdwData.value
	else: return False

# bool CgosIOSetDirection(HCGOS hCgos, unsigned long dwUnit, unsigned long dwData)
def ioSetDirection(dwUnit, dwData):
	_cgos.CgosIOSetDirection.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosIOSetDirection.restype = ctypes.c_bool
	return _cgos.CgosIOSetDirection(hCgos, dwUnit, dwData)

# cgosret_bool CgosIOGetNameA(HCGOS hCgos, unsigned int dwUnit, char *pszName, unsigned int dwSize);
'''
MOD001 v

def ioGetName(dwUnit):
	_cgos.CgosIOGetNameA.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint)
	_cgos.CgosIOGetNameA.restype = ctypes.c_bool
	dwSize = ctypes.c_ulong(128)
	pszName = ctypes.create_string_buffer(dwSize.value)
	if _cgos.CgosIOGetNameA(hCgos, dwUnit, pszName, dwSize) == True: return pszName.value
	else: return False
	
MOD001 ^

'''
	###################################
	#####   FUNCTION GROUP WDOG   #####
	###################################

CGOS_WDOG_EVENT_MAX_STAGES = 3

class CGOSWDSTAGE (ctypes.Structure):
	_fields_ = [
		('dwTimeout', ctypes.c_uint32),
		('dwEvent', ctypes.c_uint32),
	]

class CGOSWDCONFIG(ctypes.Structure):
	_fields_ = [
		('dwSize', ctypes.c_uint32),
		('dwTimeout', ctypes.c_uint32), # not used in staged mode
		('dwDelay', ctypes.c_uint32),
		('dwMode', ctypes.c_uint32),
		# optional parameters for staged watchdog
		('dwOpMode', ctypes.c_uint32),
		('dwStageCount', ctypes.c_uint32),
		('stStages',CGOSWDSTAGE * CGOS_WDOG_EVENT_MAX_STAGES),
	]

# ulong CgosWDogCount(HCGOS hCgos)
def wdogCount():
	_cgos.CgosWDogCount.argtype = ctypes.c_uint
	_cgos.CgosWDogCount.restype = ctypes.c_ulong
	return _cgos.CgosWDogCount(hCgos)

# bool CgosWDogIsAvailable(HCGOS hCgos, unsigned long dwUnit)
def wdogIsAvailable(dwUnit):
	_cgos.CgosWDogIsAvailable.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosWDogIsAvailable.restype = ctypes.c_bool
	return _cgos.CgosWDogIsAvailable(hCgos, dwUnit)

# bool CgosWDogTrigger(HCGOS hCgos, unsigned long dwUnit)
def wdogTrigger(dwUnit):
	_cgos.CgosWDogTrigger.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosWDogTrigger.restype = ctypes.c_bool
	return _cgos.CgosWDogTrigger(hCgos, dwUnit)

# bool CgosWDogGetConfigStruct(HCGOS hCgos, unsigned long dwUnit, CGOSWDCONFIG *pConfig)
def wdogGetConfigStruct(dwUnit):
	cgoswdconfig = CGOSWDCONFIG(0)
	cgoswdstage = CGOSWDSTAGE(0)
	cgoswdconfig.dwSize = (ctypes.sizeof(ctypes.c_uint32)*6) + (len((cgoswdstage._fields_) * ctypes.sizeof(ctypes.c_uint32)) * CGOS_WDOG_EVENT_MAX_STAGES)
	_cgos.CgosWDogGetConfigStruct.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosWDogGetConfigStruct.restype = ctypes.c_bool
	if (_cgos.CgosWDogGetConfigStruct(hCgos, dwUnit, ctypes.addressof(cgoswdconfig))) == True:
		results = {}
		stStages0 = {}
		stStages1 = {}
		stStages2 = {}
		for field in cgoswdconfig._fields_: results[field[0]] = getattr(cgoswdconfig, field[0])
		del results['stStages']
		results['stStages0'] = { 'dwTimeout' : cgoswdconfig.stStages[0].dwTimeout, 'dwEvent' : cgoswdconfig.stStages[0].dwEvent }
		results['stStages1'] = { 'dwTimeout' : cgoswdconfig.stStages[1].dwTimeout, 'dwEvent' : cgoswdconfig.stStages[1].dwEvent }
		results['stStages2'] = { 'dwTimeout' : cgoswdconfig.stStages[2].dwTimeout, 'dwEvent' : cgoswdconfig.stStages[2].dwEvent }
		return results
	else : return False

# bool CgosWDogSetConfigStruct(HCGOS hCgos, unsigned long dwUnit, CGOSWDCONFIG *pConfig)
def wdogSetConfigStruct(dwUnit, pConfig):
	cgoswdconfig = CGOSWDCONFIG(0)
	cgoswdstage = CGOSWDSTAGE(0)


	cgoswdconfig.dwSize = ((ctypes.sizeof(ctypes.c_uint32)*6) + ((len(cgoswdstage._fields_) * ctypes.sizeof(ctypes.c_uint32)) * CGOS_WDOG_EVENT_MAX_STAGES))
	if 'dwTimeout' in pConfig: cgoswdconfig.dwTimeout = pConfig['dwTimeout']
	if 'dwDelay' in pConfig: cgoswdconfig.dwDelay = pConfig['dwDelay']
	if 'dwMode' in pConfig: cgoswdconfig.dwMode = pConfig['dwMode']
	if 'dwOpMode' in pConfig: cgoswdconfig.dwOpMode = pConfig['dwOpMode']
	if 'dwStageCount' in pConfig: cgoswdconfig.dwStageCount = pConfig['dwStageCount']
	if 'stStages0' in pConfig:
		if 'dwTimeout' in pConfig['stStages0']: cgoswdconfig.stStages[0].dwTimeout = pConfig['stStages0']['dwTimeout']
		if 'dwEvent' in pConfig['stStages0']: cgoswdconfig.stStages[0].dwEvent = pConfig['stStages0']['dwEvent']
	if 'stStages1' in pConfig:
		if 'dwTimeout' in pConfig['stStages1']: cgoswdconfig.stStages[1].dwTimeout = pConfig['stStages1']['dwTimeout']
		if 'dwEvent' in pConfig['stStages1']: cgoswdconfig.stStages[1].dwEvent = pConfig['stStages1']['dwEvent']
	if 'stStages2' in pConfig:
		if 'dwTimeout' in pConfig['stStages2']: cgoswdconfig.stStages[2].dwTimeout = pConfig['stStages2']['dwTimeout']
		if 'dwEvent' in pConfig['stStages2']: cgoswdconfig.stStages[2].dwEvent = pConfig['stStages2']['dwEvent']
	#_cgos.CgosWDogGetConfigStruct.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp) MOD003
	_cgos.CgosWDogGetConfigStruct.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_void_p)
	_cgos.CgosWDogGetConfigStruct.restype = ctypes.c_bool
	cgoswdconfig = ctypes.cast(ctypes.pointer(cgoswdconfig), ctypes.POINTER(ctypes.c_void_p)) #MOD003
	#return (_cgos.CgosWDogSetConfigStruct(hCgos, dwUnit, ctypes.addressof(cgoswdconfig))) MOD003
	return (_cgos.CgosWDogSetConfigStruct(hCgos, dwUnit, cgoswdconfig)) #MOD003

# bool CgosWDogSetConfig(HCGOS hCgos, unsigned long dwUnit, unsigned long timeout, unsigned long delay, unsigned long mode)
def wdogSetConfig(dwUnit, timeout, delay, mode):
	_cgos.CgosWDogSetConfig.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong)
	_cgos.CgosWDogSetConfig.restype = ctypes.c_bool
	return _cgos.CgosWDogSetConfig(hCgos, dwUnit, timeout, delay, mode)
# bool CgosWDogDisable(HCGOS hCgos, unsigned long dwUnit)
def wdogDisable(dwUnit):
	_cgos.CgosWDogDisable.argtypes = (ctypes.c_uint, ctypes.c_ulong)
	_cgos.CgosWDogDisable.restype = ctypes.c_bool
	return _cgos.CgosWDogDisable(hCgos, dwUnit)

# bool CgosWDogGetInfo(HCGOS hCgos, unsigned long dwUnit, CGOSWDINFO *pInfo)
def wdogGetInfo(dwUnit):
	
	class CGOSWDINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('dwMinTimeout', ctypes.c_uint32),
			('dwMaxTimeout', ctypes.c_uint32),
			('dwMinDelay', ctypes.c_uint32),
			('dwMaxDelay', ctypes.c_uint32),
			('dwOpModes',  ctypes.c_uint32), # supported operation mode mask (1<<opmode)
			('dwMaxStageCount', ctypes.c_uint32),
			('dwEvents', ctypes.c_uint32), # supported event mask (1<<event)
			('dwType', ctypes.c_uint32),
		]
	
	cgoswdinfo = CGOSWDINFO(0)
	cgoswdinfo.dwSize = len((cgoswdinfo._fields_) * ctypes.sizeof(ctypes.c_uint32))
	_cgos.CgosWDogGetInfo.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosWDogGetInfo.restype = ctypes.c_bool 
	if (_cgos.CgosWDogGetInfo(hCgos, dwUnit, ctypes.addressof(cgoswdinfo))) == True:
		results = {}
		for field in cgoswdinfo._fields_: results[field[0]] = getattr(cgoswdinfo, field[0])
		return results
	else: return False

	##########################################
	#####   FUNCTION GROUP TEMPERATURE   #####
	##########################################

# ulong CgosTemperatureCount(HCGOS hCgos)
def temperatureCount():
	_cgos.CgosTemperatureCount.argtype = ctypes.c_uint
	_cgos.CgosTemperatureCount.restype = ctypes.c_ulong
	return _cgos.CgosTemperatureCount(hCgos)

# bool CgosTemperatureGetInfo(HCGOS hCgos, unsigned long dwUnit, CGOSTEMPERATUREINFO *pInfo)
def temperatureGetInfo(dwUnit):
	# Temperature in units of 1/1000th degrees celcius
	class CGOSTEMPERATUREINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwType', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('dwAlarm', ctypes.c_uint32),
			('dwRes', ctypes.c_uint32),
			('dwMin', ctypes.c_uint32),
			('dwMax', ctypes.c_uint32),
			('dwAlarmHi', ctypes.c_uint32),
			('dwHystHi', ctypes.c_uint32),
			('dwAlarmLo', ctypes.c_uint32),
			('dwHystLo', ctypes.c_uint32),
		]
	cgostemperatureinfo = CGOSTEMPERATUREINFO(0)
	cgostemperatureinfo.dwSize = len((cgostemperatureinfo._fields_) * ctypes.sizeof(ctypes.c_uint32))
	_cgos.CgosTemperatureGetInfo.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosTemperatureGetInfo.restype = ctypes.c_bool
	if (_cgos.CgosTemperatureGetInfo(hCgos, dwUnit, ctypes.addressof(cgostemperatureinfo))) == True:
		results = {}
		for field in cgostemperatureinfo._fields_: results[field[0]] = getattr(cgostemperatureinfo, field[0])
		results['dwRes'] = ((ctypes.c_int)(results['dwRes'])).value
		results['dwMax'] = ((ctypes.c_int)(results['dwMax'])).value
		results['dwMin'] = ((ctypes.c_int)(results['dwMin'])).value
		results['dwAlarmHi'] = ((ctypes.c_int)(results['dwAlarmHi'])).value
		results['dwAlarmLo'] = ((ctypes.c_int)(results['dwAlarmLo'])).value
		results['dwHystHi'] = ((ctypes.c_int)(results['dwHystHi'])).value
		results['dwHystLo'] = ((ctypes.c_int)(results['dwHystLo'])).value
		return results
	else: return False

# bool CgosTemperatureGetCurrent(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting, unsigned long *pdwStatus)
def temperatureGetCurrent(dwUnit):
	_cgos.CgosTemperatureGetCurrent.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosTemperatureGetCurrent.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	pdwStatus = ctypes.c_ulong(0)
	if _cgos.CgosTemperatureGetCurrent(hCgos, dwUnit, ctypes.byref(pdwSetting), ctypes.byref(pdwStatus)) == True: 
		results = {'pdwSetting' : pdwSetting.value, 'pdwStatus' : pdwStatus.value}
		return results
	else: return False

	##################################
	#####   FUNCTION GROUP FAN   #####
	##################################	

# ulong CgosFanCount(HCGOS hCgos)
def fanCount():
	_cgos.CgosFanCount.argtype = ctypes.c_uint
	_cgos.CgosFanCount.restype = ctypes.c_ulong
	return _cgos.CgosFanCount(hCgos)

# bool CgosFanGetInfo(HCGOS hCgos, unsigned long dwUnit, CGOSFANINFO *pInfo)
def fanGetInfo(dwUnit):
	# Fan speed values in RPM (revolutions per minute)
	class CGOSFANINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwType', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('dwAlarm', ctypes.c_uint32),
			('dwSpeedNom', ctypes.c_uint32),
			('dwMin', ctypes.c_uint32),
			('dwMax', ctypes.c_uint32),
			('dwAlarmHi', ctypes.c_uint32),
			('dwHystHi', ctypes.c_uint32),
			('dwAlarmLo', ctypes.c_uint32),
			('dwHystLo', ctypes.c_uint32),
			('dwOutMin', ctypes.c_uint32),
			('dwOutMax', ctypes.c_uint32),
		]
	cgosfaninfo = CGOSFANINFO(0)
	cgosfaninfo.dwSize = len((cgosfaninfo._fields_) * ctypes.sizeof(ctypes.c_uint32))
	_cgos.CgosFanGetInfo.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosFanGetInfo.restype = ctypes.c_bool
	if (_cgos.CgosFanGetInfo(hCgos, dwUnit, ctypes.addressof(cgosfaninfo))) == True:
		results = {}
		for field in cgosfaninfo._fields_: results[field[0]] = getattr(cgosfaninfo, field[0])
		results['dwSpeedNom'] = ((ctypes.c_int)(results['dwSpeedNom'])).value
		results['dwMax'] = ((ctypes.c_int)(results['dwMax'])).value
		results['dwMin'] = ((ctypes.c_int)(results['dwMin'])).value
		results['dwAlarmHi'] = ((ctypes.c_int)(results['dwAlarmHi'])).value
		results['dwAlarmLo'] = ((ctypes.c_int)(results['dwAlarmLo'])).value
		results['dwHystHi'] = ((ctypes.c_int)(results['dwHystHi'])).value
		results['dwHystLo'] = ((ctypes.c_int)(results['dwHystLo'])).value
		results['dwOutMin'] = ((ctypes.c_int)(results['dwOutMin'])).value
		results['dwOutMax'] = ((ctypes.c_int)(results['dwOutMax'])).value
		return results
	else: return False

# bool CgosFanGetCurrent(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting, unsigned long *pdwStatus)
def fanGetCurrent(dwUnit):
	_cgos.CgosFanGetCurrent.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosFanGetCurrent.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	pdwStatus = ctypes.c_ulong(0)
	if _cgos.CgosFanGetCurrent(hCgos, dwUnit, ctypes.byref(pdwSetting), ctypes.byref(pdwStatus)) == True:
		results = {'pdwSetting' : pdwSetting.value, 'pdwStatus' : pdwStatus.value}
		return results
	else: return False

	######################################
	#####   FUNCTION GROUP VOLTAGE   #####
	######################################

# ulong CgosVoltageCount(HCGOS hCgos)
def voltageCount():
	_cgos.CgosVoltageCount.argtype = ctypes.c_uint
	_cgos.CgosVoltageCount.restype = ctypes.c_ulong
	return _cgos.CgosVoltageCount(hCgos)

# bool CgosVoltageGetInfo(HCGOS hCgos, unsigned long dwUnit, CGOSVOLTAGEINFO *pInfo)
def voltageGetInfo(dwUnit):
	# Voltage in units of 1/1000th volt
	class CGOSVOLTAGEINFO(ctypes.Structure):
		_fields_ = [
			('dwSize', ctypes.c_uint32),
			('dwType', ctypes.c_uint32),
			('dwNom', ctypes.c_uint32),
			('dwFlags', ctypes.c_uint32),
			('dwAlarm', ctypes.c_uint32),
			('dwRes', ctypes.c_uint32),
			('dwMin', ctypes.c_uint32),
			('dwMax', ctypes.c_uint32),
			('dwAlarmHi', ctypes.c_uint32),
			('dwHystHi', ctypes.c_uint32),
			('dwAlarmLo', ctypes.c_uint32),
			('dwHystLo', ctypes.c_uint32),
		]
	cgosvoltageinfo = CGOSVOLTAGEINFO(0)
	cgosvoltageinfo.dwSize = len((cgosvoltageinfo._fields_) * ctypes.sizeof(ctypes.c_uint32))
	_cgos.CgosVoltageGetInfo.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.c_voidp)
	_cgos.CgosVoltageGetInfo.restype = ctypes.c_bool
	if (_cgos.CgosVoltageGetInfo(hCgos, dwUnit, ctypes.addressof(cgosvoltageinfo))) == True:
		results = {}
		for field in cgosvoltageinfo._fields_: results[field[0]] = getattr(cgosvoltageinfo, field[0])
		results['dwRes'] = ((ctypes.c_int)(results['dwRes'])).value
		results['dwNom'] = ((ctypes.c_int)(results['dwNom'])).value
		results['dwMax'] = ((ctypes.c_int)(results['dwMax'])).value
		results['dwMin'] = ((ctypes.c_int)(results['dwMin'])).value
		results['dwAlarmHi'] = ((ctypes.c_int)(results['dwAlarmHi'])).value
		results['dwAlarmLo'] = ((ctypes.c_int)(results['dwAlarmLo'])).value
		results['dwHystHi'] = ((ctypes.c_int)(results['dwHystHi'])).value
		results['dwHystLo'] = ((ctypes.c_int)(results['dwHystLo'])).value
		return results
	else: return False

# bool CgosVoltageGetCurrent(HCGOS hCgos, unsigned long dwUnit, unsigned long *pdwSetting, unsigned long *pdwStatus)
def voltageGetCurrent(dwUnit):
	_cgos.CgosVoltageGetCurrent.argtypes = (ctypes.c_uint, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))
	_cgos.CgosVoltageGetCurrent.restype = ctypes.c_bool
	pdwSetting = ctypes.c_ulong(0)
	pdwStatus = ctypes.c_ulong(0)
	if _cgos.CgosVoltageGetCurrent(hCgos, dwUnit, ctypes.byref(pdwSetting), ctypes.byref(pdwStatus)) == True:
		results = {'pdwSetting' : pdwSetting.value, 'pdwStatus' : pdwStatus.value}
		return results
	else: return False

	##########################################################
	#####   CGOS.PY SPECIFIC FUNCTIONS FOR CONVENIENCE   #####
	##########################################################

# Open the CGOS interface using only one command
def openif():
	if libInitialize() == False:
		if libInstall(1) == False:
			print ("ERROR: Failed to install CGOS interface.") #MOD003
			return False
		if libInitialize() == False:
			print ("ERROR: Failed to initialize CGOS interface.") #MOD003
			return False
	if boardOpen(0,0,0) == False:
		print ("Could not open a board.") #MOD003
		return False
	return True

# Close the CGOS interface using only one command
def closeif():
	if boardClose() == False:
		print ("ERROR: Failed to close CGOS interface.") #CGMOD003
		return False
	if libUninitialize() == False:
		print ("ERROR: Failed to un-initialize CGOS interface.") #CGMOD003
		return False
	return True

// LibOsa.h
// CGOS OS Abstraction Layer
// {G)U(2} 2005.01.19

//***************************************************************************

#ifndef _LIBOSA_H_
#define _LIBOSA_H_

//***************************************************************************

#define CGOS_INVALID_HANDLE ((void *)-1)

//***************************************************************************

unsigned int OsaInstallDriver(unsigned int install);
void *OsaOpenDriver(void);
void OsaCloseDriver(void *hDriver);
unsigned int OsaDeviceIoControl(void *hDriver, unsigned long dwIoControlCode,
    void *pInBuffer, unsigned long nInBufferSize,
    void *pOutBuffer, unsigned long nOutBufferSize,
    unsigned long *pBytesReturned);

//***************************************************************************

void *OsaMemAlloc(unsigned long len);
void OsaMemFree(void *p);
void OsaMemCpy(void *d, void *s, unsigned long len);
void OsaMemSet(void *d, char val, unsigned long len);

//***************************************************************************

#endif


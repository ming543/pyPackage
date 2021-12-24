// LibOsaM.c
// CGOS OS Abstraction Memory
// {G)U(2} 2005.01.19

//***************************************************************************

//#include "CgosLib.h"
#include <stdlib.h>
#include <memory.h>
#include "LibOsa.h"    // CGOS OS Abstraction Layer

//***************************************************************************

void *OsaMemAlloc(unsigned long len)
  {
  return malloc(len);
  }

void OsaMemFree(void *p)
  {
  free(p);
  }

void OsaMemCpy(void *d, void *s, unsigned long len)
  {
  memcpy(d,s,len);
  }

void OsaMemSet(void *d, char val, unsigned long len)
  {
  memset(d,val,len);
  }

//***************************************************************************

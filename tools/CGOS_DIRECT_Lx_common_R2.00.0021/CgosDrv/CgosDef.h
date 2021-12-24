// CgosDef.h
// CGOS library header files
// {G)U(2} 2005.06.22

//***************************************************************************

#ifndef _CGOSDEF_H_
#define _CGOSDEF_H_

//***************************************************************************

#ifndef FALSE
#define FALSE 0
#endif

#ifndef TRUE
#define TRUE 1
#endif

#ifndef NULL
#define NULL ((void *)0)
#endif

//***************************************************************************

// just to have an option
#ifdef DEF_WCHAR_T
#define wchar_t short
#endif

//***************************************************************************

#ifndef dbpf
#define dbpf(s)
#endif

//***************************************************************************

#endif

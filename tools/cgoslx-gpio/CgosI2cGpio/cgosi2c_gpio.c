/************************************************************************************
1、本程序专门测试PCA9555，I2C转GPIO功能
2、本程序在TCA模块中测试通过，TCA PCA955地址：0X4E
版本：V.0
测试者：ANDY
测试时间：12/11/27
----------------------------------------------
PCA9555测试命令：
Command     Register
  0        Input port 0
  1        Input port 1
  2        Output port 0
  3        Output port 1
  4        Polarity inversion port 0
  5        Polarity inversion port 1
  6        Configuration port 0
  7        Configuration port 1
--------------------------------------------------------------
Registers 0 and 1 — Input Port Registers
  bit    I0.7  I0.6  I0.5  I0.4  I0.3  I0.2  I0.1 IO.0
default    X     X     X     X     X    X      X    X
  bit   I1.7   I1.6  I1.5  I1.4  I1.3  I1.2  I1.1  I1.0
default   X      X     X     X     X    X      X    X
--------------------------------------------------------------
Registers 2 and 3 — Output Port Registers
  bit   O0.7   O0.6   O0.5   O0.4   O0.3   O0.2   O0.1   O0.0
default   1      1      1      1      1      1     1      1
  bit   O1.7   O1.6   O1.5   O1.4   O1.3   O1.2   O1.1   O1.0
default   1      1      1      1      1      1      1      1
---------------------------------------------------------------
Registers 4 and 5 — Polarity Inversion Registers
  bit    N0.7   N0.6   N0.5   N0.4   N0.3   N0.2   N0.1   N0.0
default    0      0      0      0      0      0      0      0
  bit    N1.7   N1.6   N1.5   N1.4   N1.3   N1.2   N1.1   N1.0
default    0      0      0      0      0      0      0      0
---------------------------------------------------------------
Registers 6 and 7 — Configuration Registers
  bit    C0.7   C0.6   C0.5   C0.4   C0.3   C0.2   C0.1   C0.0
default    1      1      1      1      1      1      1      1
  bit    C1.7   C1.6   C1.5   C1.4   C1.3   C1.2   C1.1   C1.0
default    1      1      1      1      1      1      1      1
*************************************************************************************/

#include "OsAL.h"
#include <stdio.h>

#include "Cgos.h"

char buf[512];

#undef TEXT

#ifndef TEXT
#define TEXT(s) s
#endif

void report(char *s)
{
  __report("%s",s);
}


int main(int argc, char* argv[])
{
	HCGOS hCgos = 0;
	

	// install the library
	if (!CgosLibInitialize())
	{
		if (!CgosLibInstall(1))
		{
			// error: can't install cgos library
			report(TEXT("Error: can't install CGOS library !\n"));
			return (-1);
		}
    report(TEXT("The driver has been installed.\n"));
    if (!CgosLibInitialize()) {
      report(TEXT("Still could not open driver, a reboot might be required!\n"));
      return (-1);
      }		
	}
	

	
    // open the cgos board
    if (CgosBoardOpen(0,0,0,&hCgos))
    {
	   report(TEXT("open CGOS board\n"));
	   
	unsigned char bAddr=0x4e; 
	unsigned char port1out[2];
	unsigned char port0config[2];
	unsigned char port1config[2];
	unsigned char port0input[1];
	unsigned char port0addr[1];;
	port0config[0]=0x06;
	port0config[1]=0xff;
	port1config[0]=0x07;
	port1config[1]=0x00;
	port1out[0]=0x03;
	port0addr[0]=0x00;
	

//=====config pac9555
	if( CgosI2CWrite(hCgos,0,bAddr,port0config,2) & CgosI2CWrite(hCgos,0,bAddr,port1config,2) ) 

	{
		report(TEXT("pac9555 config OK\n"));
	}
	else
	{
		report(TEXT("pac9555 config fail\n"));
	}
 report(TEXT("----------------------port1.1~8bit output-------------------------\n"));
//PORT1 8bit 输出，8个输出端口用16进制数表示，例如0x01代表输出端口1输出高电平，0xff代表8个输出端口输出高电平	
		port1out[1]=0x01;
		if( CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit1 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x02;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit2 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x04;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit3 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x08;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit4 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x10;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit5 output 1\n"));	
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x20;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit6 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x40;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit7 output 1\n"));
				Sleep (1000);//延时100MS 
			}

		port1out[1]=0x80;
		if(CgosI2CWrite(hCgos,0,bAddr,port1out,2)) 
			{
				report(TEXT("bit8 output 1\n"));	
				Sleep (1000);//延时100MS 
			}
//读取输入值， Port0.0至Port0.7为输入端口，8端口使用16进制数表示，例如读到数值0xff表示所有输入IO口为高电平，0x01表示端口2至7为低电平端口1高电平（默认所有输入端口都为高电平）
 	 if( CgosI2CWriteReadCombined(hCgos,0,bAddr,port0addr, 1, port0input, 1))
 	 	{
 	 		report(TEXT("----------------------port0.1~8bit  1nput-------------------------\n"));
 	 		printf("input:%02x\n",port0input[0]);
 	 	}


  }
  else
  {
	// error: can't open board
	report(TEXT("Error: can't open CGOS board !\n"));
	return (-1);
  }	
	   
  CgosBoardClose(hCgos);

  return 0;
}



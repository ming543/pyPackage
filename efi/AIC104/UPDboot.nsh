## -a Last SMbus Slave Address (default: 50)
## -A Current SMbus Slave Address (default: 66)
## -b / -B Update Boot with Bootfile
## -i Last I2C Slave Address (default: 50)
## -I Current I2C Slave Address (default: 66)
## -e Wait time (ms) after Erase Flash (default: 9)
## -d Wait time (ms) after Send 0x21 Commmnad (default: 1.5)
## -s Wait time (ms) for exist and start Enter Bootloader (default: 400)
## -p Wait time (ms) for PCH GPIO Switch on 10 times (default: 1)
## -u Wait time (ms) after Successfully downloaded on 10 times (default: 10)
## -P Power mode turn to ATX S5

@aicflash -b BOOT.bin -P

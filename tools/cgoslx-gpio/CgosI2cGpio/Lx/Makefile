PROJECT_INC = -I. -I.. -I../.. -I../../CgosLib
PROJECT_LIB = -lcgos -L../../CgosLib/Lx
C_source = ../cgosi2c_gpio.c
OPT = -Wall

default:
	gcc $(C_source) -o cgosi2c_gpio $(OPT) $(DEF) $(PROJECT_INC) $(PROJECT_LIB)

clean:
	rm -f cgosmon

cleanall: clean


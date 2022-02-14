#!/bin/bash
LOC="/home/production"
CGUT_LOC="$LOC/hw_test/tools/cgutillx/cgutlcmd"
BIOS_REV=$(sudo $CGUT_LOC/cgutlcmd CGINFO /OT:BOARD /DUMP /BIOS | grep "System BIOS" | awk '{print $4}')

$CGUT_LOC/cgutlcmd module /ot:board /save /of:$BIOS_REV.MO1 /t:1 
sleep 1

$CGUT_LOC/cgutlcmd module /ot:board /create /if:$BIOS_REV.MO1 /of:$BIOS_REV.MOD /t:2

NEWFILE=`echo $BIOS_REV.MOD | sed 's/R/W/g'`
mv $BIOS_REV.MOD $NEWFILE
rm $BIOS_REV.MO1


@echo -off
;mode 80 25
;foundimage section is simply to locate the correct drive
cls
if exist fs0:\AUTOEXEC.MAN then
    fs0:
	echo Found Update Packages on fs0:
	goto FOUNDIMAGE
endif
if exist fs1:\AUTOEXEC.MAN then
	fs1:
	echo Found Update Packages on fs1:
	goto FOUNDIMAGE
endif
if exist fs2:\AUTOEXEC.MAN then
	fs2:
	echo Found Update Packages on fs2:
	goto FOUNDIMAGE
endif
	echo "Unable to find Update Packages".
	echo "Please mount the drive with the update package".
	echo ""
 goto END

:FOUNDIMAGE
echo "============================================================="
echo "This utility will allow you to update the BIOS and firmware."
echo "If you want to do all these functions, press Enter. If not, hit 'q'."
echo ""
echo "AIC104.nsh - Update AIC FW to REV:1.04"
echo "AICCFG.nsh - Program the AIC config by PN. AICCFG.nsh 20010-000001.A.0 "
echo "V2C120.nsh - Update V2C/AIM BIOS to REV:1.20 , Disable BIOS lock before update."
echo "V2CE120.nsh - Update V2CE/AIML BIOS to REV:1.20 , Disable BIOS lock before update."
echo "V3C120.nsh - Update V3C/AIH BIOS to REV:1.20 , Disable BIOS lock before update."
echo "============================================================="

ls *.nsh
:pause
echo ""
echo ""

:END
fs0:
cd efiScript
cd q715
eeupdate64e.efi /PCIINFO /ALL
stall 1000000 #delay 1000000us
echo "Please check NIC1&NIC2 exist, Press any key continue..."
pause -q

if not exist fs0:\q715.flg then
    echo "Program I210"
	#I210 port1
    eeupdate64e.efi /NIC=1 /D=Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin
    stall 1000000 #delay 1000000us
	type pass > q715.flg
else
    echo "program MAC"
	type MAC.DAT
	echo "Please check MAC, Press any key continue..."
    pause -q
	eeupdate64e.efi /NIC=1 /D=Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin /a mac.dat
    incmac.efi
    eeupdate64e.efi /NIC=1 /calcchksum
    stall 1000000 #delay 1000000us
	del fs0:\q715.flg
endif

#cd \
#cd bootup_uefi
#bootup.efi

#Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin
#I210 port1
#eeupdate64e.efi /NIC=1 /FILE=NONIOI.bin /a mac.dat

eeupdate64e.efi /NIC=1 /D=Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin /a mac.dat
incmac.efi
eeupdate64e.efi /NIC=1 /calcchksum
stall 1000000 #delay 1000000us


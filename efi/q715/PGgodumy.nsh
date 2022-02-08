#I219LM port1  
#eeupdate64e.efi /NIC=1 /FILE=n8_whl_lp_lm_non_lan_sw_v0.4.txt /a mac.dat
#incmac.efi
#pause

#I210 port1
eeupdate64e.efi /NIC=1 /FILE=Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin
stall 1000000 #delay 1000000us


#I210 port2
#eeupdate64e.efi /NIC=2 /FILE=Dev_Start_I210_Copper_NOMNG_4Mb_A2_3.25_0.03.bin



#I211
#eeupdate64e.efi /NIC=2 /FILE=I211nvm.txt /a mac.dat /invmupdate
#incmac.efi
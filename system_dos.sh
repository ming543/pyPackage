#!/bin/bash
# Script for stux system setup by EFCO Sam

userFolder="/home/stux"
pyFolder="/home/stux/pyPackage"
dosFolder="/usr/lib/live/mount/persistence/sda1"
#cd $dosFolder && sudo git init
#cd $dosFolder && sudo git remote add origin https://github.com/ming543/V23C_DOS.git

sudo apt-get install -y tofrodos

#MBR更新由other-test 執行
#sudo dd if=/usr/lib/syslinux/mbr/mbr.bin of=/dev/sda

cd $dosFolder && sudo find . -type f \( -name '*.BAT' -o -name '*.TXT' \) -exec todos -v '{}' \;
sudo cp $pyFolder/efi/startup.nsh $dosFolder/startup.nsh

echo "****** system setup update done ******"
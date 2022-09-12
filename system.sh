#!/bin/bash
# Script for stux system setup by EFCO Sam

userFolder="/home/stux"
pyFolder="/home/stux/pyPackage"
dosFolder="/usr/lib/live/mount/persistence/sda1/"
#cd $dosFolder && sudo git init
#cd $dosFolder && sudo git remote add origin https://github.com/ming543/V23C_DOS.git

sudo cp $userFolder/.gitconfig /root/
sudo cp $userFolder/.git-credentials /root/
sudo cp $pyFolder/tools/11-ftdi.rules /etc/udev/rules.d/11-ftdi.rules

sudo apt-get install -y tofrodos
sudo apt-get install -y sshpass
sudo apt-get install -y tmux
sudo apt-get install -y stress-ng
sudo apt-get install libusb-1.0
sudo apt-get install clonezilla

#fix 1min30s issue
sudo sed -i 's/#DefaultTimeoutStartSec=90s/DefaultTimeoutStartSec=1s/g' /etc/systemd/system.conf
sudo sed -i 's/#DefaultTimeoutStopSec=90s/DefaultTimeoutStopSec=1s/g' /etc/systemd/system.conf
sudo sed -i 's/#DefaultRestartSec=100ms/DefaultRestartSec=100ms/g' /etc/systemd/system.conf

echo "****** system setup update done ******"

#!/bin/bash
# Script for stux system setup by EFCO Sam

userFolder = "/home/stux"
pyFolder = "/home/stux/pyPackage/"
dosFolder = "/usr/lib/live/mount/persistence/sda1/"
cd $dosFolder && sudo git init
cd $dosFolder && sudo git remote add origin https://github.com/ming543/V23C_DOS.git
cd $dosFolder && sudo git fetch --all
sudo cp $userFolder/.gitconfig /root/
sudo cp $userFolder/.git-credentials /root/
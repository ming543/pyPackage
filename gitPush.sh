#!/bin/bash
git pull
git add .
git commit -m "$1"
git branch -M main
git push -u origin main

pLocal=/home/mm/pyPackage/
pCloud=/home/mm/pCloudDrive/pyPackage/
if [ -d $pCloud ];then
	rsync -avh $pLocal $pCloud
	echo "****** pCloud update done ******"
fi

wslLocal=/home/ming/pyPackage/
wslCloud=/home/ming/pCloudDrive/pyPackage/
if [ -d $wslCloud  ];then
        rsync -avh $wslLocal $wslCloud
	echo "****** wslCloud update done ******"
fi

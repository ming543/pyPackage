#!/bin/bash
git pull
git add .
git commit -m "$1"
git branch -M main
git push -u origin main

pcloudcc -u sam.lee@efcotec.com -d
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

stuxLocal=/home/stux/pyPackage/
stuxCloud=/home/stux/pCloudDrive/pyPackage/
if [ -d $stuxCloud  ];then
        rsync -avh $stuxLocal $stuxCloud
	echo "****** stuxCloud update done ******"
fi

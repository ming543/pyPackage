#!/bin/bash

#rclone -v sync /home/stux/pyPackage/ pcloud:pyPackage --exclude=/.git/** -L -P
rclone -v copy /home/stux/pyPackage/ pcloud:pyPackage --exclude=/.git/** -L -P

pyLocal=/home/stux/pyPackage/
pyCloud=/home/stux/pCloudDrive/pyPackage/
#if [ -d $pyCloud ];then
#        rsync -avh --exclude '.git' --no-p --no-o --no-g $pyLocal $pyCloud
#	echo "****** pyCloud update done ******"
#fi


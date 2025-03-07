#!/bin/bash
sudo cp /etc/default/grub /etc/default/grub.bak
sudo cp ~/pyPackage/tools/grub.lm203x /etc/default/grub
sudo update-grub
sudo systemctl set-default graphical.target

LIST=`crontab -l`
SOURCE="/home/stux/pyPackage/tools/rclone_log_to_CM_EFCO.sh"
if echo "$LIST" | grep -q "$SOURCE"; then
   echo "The back job had been added.";
else
   crontab -l | { cat; echo "*/30 * * * * $SOURCE"; } | crontab -
fi

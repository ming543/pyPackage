#!/bin/bash

NETWORKID=$(sudo zerotier-cli listnetworks | tail -1 | awk '{print $3}')

sudo zerotier-cli listnetworks
if [ $? != 0 ];then
    curl -s https://install.zerotier.com | sudo bash
fi

if [ $NETWORKID != "565799d8f6928c57" ]; then
    sudo zerotier-cli join 565799d8f6928c57
fi

sudo service zerotier-one stop
sleep 2
sudo rm /var/lib/zerotier-one/identity.public
sudo rm /var/lib/zerotier-one/identity.secret
sudo service zerotier-one start
sleep 5
sudo zerotier-cli info


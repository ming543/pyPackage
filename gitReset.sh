#!/bin/bash
cd /home/production/pyPackage && git gc
cd /home/production/pyPackage && git fetch --all
cd /home/production/pyPackage && git reset --hard
cd /home/production/pyPackage && git clean -f -d
cd /home/production/pyPackage && git pull


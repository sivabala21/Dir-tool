#!/bin/bash
#To install Dirpy File
apt update -y && apt upgrade -y
apt install python python2 git curl
clear
echo -e "			\e[33;1mDownloading\e[0m \n"
sleep 2

curl -LO https://srv-file7.gofile.io/download/19zLo4/Dirpy.py
clear
echo -e "            		\e[31;1mRunning\e[0m       "
sleep 2
clear
python Dirpy.py



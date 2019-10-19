#! /bin/bash
#
#
apt update -y && apt upgrade -y
apt install python python2 git curl
cd $HOME
echo "          Download"

curl -LO https://srv-file7.gofile.io/download/eaNDXc/Dirpy.py
echo "          Runing..."

python Dirpy.py
#
#
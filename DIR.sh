#! /bin/bash
#
#
apt update -y && apt upgrade -y
apt install python python2 git curl
cd $HOME
echo "          Download"
git clone https://github.com/BOT-CODER/PY_CODER.git
cd PY_CODER/
echo "          Runing..."
python Dirpy.py
#
#

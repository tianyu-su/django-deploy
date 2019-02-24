#!/bin/bash 
sudo apt-get install -y gcc make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

sudo mkdir /etc/python<python-version>

sudo wget -P /home/$USER https://www.python.org/ftp/python/<python-version>/Python-<python-version>.tgz 

sudo tar zxvf  /home/$USER/Python-<python-version>.tgz -C  /home/$USER
sudo rm /home/$USER/Python-<python-version>.tgz

cd /home/$USER/Python-<python-version>
sudo ./configure --enable-optimizations --prefix=/etc/python<python-version>

sudo make 
sudo make install

sudo virtualenv --python=/etc/python<python-version>/bin/python3 --no-site-packages --download /home/.pyenvs/<web-name>
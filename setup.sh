!# /usr/bin/env bash

sudo apt-get update
sudo apt-get install python3-pip
pip3 install requests
pip3 install selenium
pip3 install json
pip3 install flask
pip3 install Flask-Uploads
sudo apt-get install sqlite3
pip3 install pprint
sh -c 'echo "set const" >> .nanorc'
sh -c 'echo "set tabsize 4" >> .nanorc'
sh -c 'echo "set tabstospaces" >> .nanorc'
sudo apt-get -y install firewalld
sudo apt-get -y install ntp
sudo apt-get -y nginx

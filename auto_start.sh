#!/bin/bash
sudo mkdir /opt/python_pic/
sudo mkdir /opt/python_pic/python_jpg/
sudo cp pic.py /opt/python_pic/
sudo cp run.sh /opt/python_pic/
sudo cp wallpaper.sh /opt/python_pic
sudo cp pic.service /etc/systemd/system
sudo pip install requests
sudo pip install beautifulsoup4
sudo chmod 777 /etc/systemd/system/pic.service
sudo chmod a+x /opt/python_pic/run.sh
sudo chmod a+x /opt/python_pic/wallpaper.sh
sudo sh -c 'echo  "screen -dm bash -c \"/opt/python_pic/wallpaper.sh\"" >> /etc/profile'
systemctl daemon-reload
systemctl start pic.service
systemctl enable pic.service

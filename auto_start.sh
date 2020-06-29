#!/bin/bash
sudo mkdir /opt/python_pic/
sudo mkdir /opt/python_pic/python_jpg/
sudo cp pic.py /opt/python_pic/
sudo cp run.sh /opt/python_pic/
sudo pip install requests
sudo pip install beautifulsoup4
sudo chmod a+x copy.sh
sudo chmod a+x run.sh
chmod a+x wallpaper.sh
sudo chmod 777 pic.service
sudo cp pic.service /etc/systemd/system
systemctl daemon-reload
systemctl start pic.service
systemctl enable pic.service

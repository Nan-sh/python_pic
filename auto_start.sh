#!/bin/bash
sudo chmod a+x copy.sh
sudo chmod a+x run.sh
sudo ./copy.sh
sudo chmod 777 pic.service
sudo cp pic.service /etc/systemd/system
systemctl daemon-reload
systemctl start pic.service
systemctl enable pic.service

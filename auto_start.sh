#!/bin/bash
sudo chmod a+x copy.sh
sudo chmod a+x run.sh
sudo ./copy.sh
sudo cp pic.service /etc/systemd/system
systemctl start pic.service
systemctl enable pic.service

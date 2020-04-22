#!/bin/bash
sudo cp pic.service /etc/systemd/system
systemctl start pic.service
systemctl enable pic.service

#!/bin/bash
sudo mv pic.service /etc/systemd/system
systemctl start pic.service
systemctl enable pic.service

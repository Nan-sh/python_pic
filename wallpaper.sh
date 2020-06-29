#!/bin/sh

while true; do
	find /opt/python_pic/python_jpg -type f \( -name 'tupian.jpg' \) -print0 | shuf -n1 -z | xargs -0 feh --bg-scale
	sleep 10m
done

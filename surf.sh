#!/bin/bash 

while true;do

pingtime=`ping -c 1 baidu.com | grep "100% packet loss" |wc -l`

if [[ $pingtime -eq 1 ]];then

	python ruc.py -u "username" -p "password"

fi

sleep 100

done

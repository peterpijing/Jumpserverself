#!/bin/bash
timenow=`date +'%M%S'`
sleep 1
timenow2=`date +'%M%S'`
timediff=$(($timenow2-$timenow))
echo $timediff
if [ $timediff -gt 1 ];then
	 

	ps -ef | grep 'python /opt/watchdog/watc*' | awk -F ' ' '{print $2}' | xargs kill -9 

	python /opt/watchdog/watchdoglisten.py 
fi

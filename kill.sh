#!/bin/bash
for i in `ps -ef|grep [s]crapy |awk '{print $2}'`
do 
	kill -9 $i
done

#!/bin/bash
for i in 1 2 3 
do
	nohup scrapy crawl Trend_spider >>logs/spider_$i.log &
	sleep 10
done

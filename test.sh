#!/bin/bash
now=`ls -l data|wc -l`
echo $now
sleep 120
end=`ls -l data|wc -l`
echo $end

#!/bin/bash
# encode
#	 ./b64.sh enc "input" 
# decode
#	./b64 "0gcm9ja3MK="

if [ $1 == "enc" ];then
	echo "$1" | base64
else
	echo "$1" | base64 --decode
fi

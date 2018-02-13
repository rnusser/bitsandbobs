#!/bin/bash

# catloc is a binary written in C by RNusser. Source file is catloc.c. 
# The purpose was to seek to the end of a large file and print the end 
# location and then seek to the new location and print contents from 
# that point

BUFFER="/tmp/web-stat-buffer"
LOCFILE="/tmp/web-stat-lastloc"
HTTPLOG="/var/log/httpd/http.log"

LASTLOC=$(head -1 $LOCFILE)

if [ "${LASTLOC}" == "" ]; then
	echo Sending zero to location file
	echo 0 > $LOCFILE
	LASTLOC=0
fi

CURLOC=$(/usr/local/bin/catloc $HTTPLOG)

if (( $CURLOC > $LASTLOC ))
then
	/usr/local/bin/catloc $LASTLOC $HTTPLOG > $BUFFER
	echo $CURLOC > $LOCFILE
else
	# Log file has rotated, thus we can wait till next time.
	echo $CURLOC > $LOCFILE
	exit 0
fi


AVG=$(cat $BUFFER | egrep -Eio "Time taken:.*"|sed s,\",,|cut -d '/' -f 2 | awk 'BEGIN {TOT = 0 } {TOT = TOT + $1} END {printf TOT/NR/1000}')
RET=$?
SAMPLES=$(cat $BUFFER | wc -l)  # Used cat as wc on it's own always shows the file name
:> $BUFFER


if (( $RET > 0 ))
then
	STATUS="ERROR"
	echo "$status web-response-time returned error"
	exit 1
fi

if (( $(echo $AVG'>'1000 | bc -l) > 0 ))  # Needed as we have a float
then
	STATUS=2
	MSG="ERROR"
else 
	STATUS=0
	MSG="OK"
fi


echo "$STATUS web-response-time response_time=$AVG;80;100;0|hits-pm=$SAMPLES $MSG $AVG ms in the last minute, $SAMPLES lines sampled"


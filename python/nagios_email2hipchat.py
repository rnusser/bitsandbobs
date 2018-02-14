#!/usr/bin/env python

# a .forward file was created to pipe the alert email to this script

import sys
import pprint
import requests
import json

room_id="xxxxxxx"
auth_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

d = {}

mylog ="""\
-----
Date: {}
To: {}
Subject: {}
Host: {}
Service: {}
Command: {}
State: {}
Output: {}
\
"""

ignoreCMD = ('check_mk-zfsget', 
            'check_mk-local',
            'check_mk-logwatch',
            ) #  Tuple

ignoreStates = ('UNKNOWN -> UNKNOWN',
                'CRITICAL -> CRITICAL',
                'OK -> OK',
                'WARNING -> WARNING',
                'WARNING -> OK',
                'OK -> WARNING',
                )

logfile="/tmp/check_mk2hipchat.log"

for line in sys.stdin:
  if ': ' in line:
    (key, val) = line.split(": ", 1)
    d[key] = val.strip()

with open(logfile, "a") as w:
  w.write(mylog.format( d['Date'], d['To'], d['Subject'], d['Host'], d['Service'], d['Command'], d['State'], d['Output']))

  if 'check_mk-logwatch' in d['Command']:
    w.write("Exit due to check_mk-logwatch\n")

  if 'PROBLEM' in d['State']:
    colour='red'

  if 'RECOVERY' in d['State']:
    colour='green'

  if 'CRITICAL -> WARNING' in d['State']:
    colour='yellow'

  # Alert only if it's regarding a web server
  if 'WEB' in d['Host'] and d['Command'] not in ignoreCMD and not any( s in d['State'] for s in ignoreStates):
    w.write("# hipchat message being sent #" + d['Subject'])
    message="Host: " + d['Host'] + " | " + "Service: " + d['Service'] + " | " + "State: " + d['State'] + " | " + "Output: " + d['Output']
    url = "https://api.hipchat.com/v2/room/"+room_id+"/notification?auth_token="+auth_token
    payload = { 'color': colour, 'message_format': 'text', 'notify': 'True', 'message': message }
    r = requests.post(url, json=payload)
    w.write("Hipchat response: " + str(r))



#!/usr/bin/env python3

import requests
import sys
import json

#define MonitorURL and Friendly Name
myMonitorURL = sys.argv[1]
friendlyName = "Monitor " + myMonitorURL

#API key for uptimerobot
API_key = sys.argv[2]


#endpoint
url = "https://api.uptimerobot.com/v2/newMonitor"
          
#concat payload with variables
payload = "api_key=" + API_key + "&format=json&type=1&url="
payload = payload + myMonitorURL
payload = payload + '&friendly_name='
payload = payload + friendlyName


headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
          
response = requests.request("POST", url, data=payload, headers=headers)

data = response.json()

if data['stat'] == 'ok':
    out_status =  print('Success! ','New monitor to add: ', myMonitorURL, ' Friendly Name: ', friendlyName  )
    print(out_status)
elif data['stat'] == 'fail':
    out_status = ('Failed. Reason', data['error']['message'])
    print(out_status)
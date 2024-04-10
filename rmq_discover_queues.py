#!/bin/env python3
import sys
import requests
import json

url = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

resp = requests.get(url + '/api/queues?page=1&page_size=500', auth=(user, password))
page_count = resp.json()['page_count']
total_count = resp.json()['total_count']

queues = []
zbx_discovery = []

if total_count <= 500:
    queues = queues + resp.json()['items']
else:
    for page in range(page_count):
        resp = requests.get(url + '/api/queues?page=' + str(page + 1) + '&page_size=500', auth=(user, password))
        queues = queues + resp.json()['items']

for queue in queues:
    zbx_discovery.append({'{#RMQ_QUEUE}':queue['name']})

print(json.dumps(zbx_discovery, indent=4))

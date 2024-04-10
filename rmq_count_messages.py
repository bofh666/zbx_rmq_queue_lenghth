#!/bin/env python3
import sys
import requests

url = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
queue = sys.argv[4]

resp = requests.get(url + '/api/queues/%2F/' + queue, auth=(user, password))
print(resp.json()['messages'])

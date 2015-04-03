#!/usr/bin/env python2

import json
import urllib2
import config

response = urllib2.urlopen(config.BASE_URL + '/nodes.json')
node_list = json.loads(response.read().decode('UTF-8'))

clients = 0
nodes = 0

for node in node_list['nodes']:
    if node['flags']['online']:
        nodes += 1
        clients += node['clientcount']

print(json.dumps({
    'nodes': nodes,
    'clients': clients
}))

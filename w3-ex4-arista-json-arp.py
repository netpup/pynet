import json


with open("arista_arp.json") as f:
    data = json.load(f)

data = data['ipV4Neighbors']

arp_entry = {}

for address in data: 
    ip_address = address['address']
    arp = address['hwAddress'] 
    arp_entry = { 
        ip_address: arp 
    } 
    print(arp_entry) 

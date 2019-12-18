import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    post_data = {"address": "192.42.42.42/32"}

    response = requests.post(
        url, headers=http_headers, data=json.dumps(post_data), verify=False
    )

    response = response.json()
    #print('json response:')
    #pprint(response)

    #status = response['status']
    #status = status['label']
    #print('=' * 10)
    #print('Status: ' + status)

    id = response['id']
    id = str(id)
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/' + id + '/'

    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

print()
print()
print('=' * 40)
#print('response.json()')
pprint(response)
print()

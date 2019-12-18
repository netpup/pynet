import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ADDRESS_ID = input("Enter Address ID to modify: ")
ADDRESS_ID = str(ADDRESS_ID)

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/' + ADDRESS_ID + '/'

    # HTTP PUT need "Content-type" header instead of accept
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # create ip address
    put_data = {"address": "192.42.42.42/32", 'description': 'The Answer'}


    response = requests.put(
        url, headers=http_headers, data=json.dumps(put_data), verify=False
    )
    response = response.json()

print()
print()
print('=' * 40)
print('IP information modified:')
print('=' * 40)
pprint(response)
print()

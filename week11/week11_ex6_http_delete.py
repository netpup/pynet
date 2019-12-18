import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    # this code was to find all the addresses I created
    # from this code i printed out all the ids.  which created a list
    # all_the_ids
    '''
    token = os.environ["NETBOX_TOKEN"]
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    # a bit of code to find all my creations
    result = response['results']
    for item in result:
        temp_dict = item['address']
        if temp_dict == '192.42.42.42/32':
            print(item['id'])
    '''
    

    #The code to remove the ids created
    all_the_ids = [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 138, 137, 136, 122, 123]


    token = os.environ["NETBOX_TOKEN"]

    for ids in all_the_ids:
        ids = str(ids)
        url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/' + ids + '/'

        http_headers = {}
        http_headers["Content-Type"] = "application/json; version=2.4;"
        http_headers["accept"] = "application/json; version=2.4;"
        http_headers["Authorization"] = f"Token {token}"

        response = requests.delete(url, headers=http_headers, verify=False)

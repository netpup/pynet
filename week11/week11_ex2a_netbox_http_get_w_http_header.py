import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    #token = $NETBOX_TOKEN
    url = "https://netbox.lasthop.io/api/"
    #url = "https://netbox.lasthop.io/api/dcim/"
    #url = "https://netbox.lasthop.io/api/dcim/devices/"
    #url = "https://api.github.com/"
    http_headers = {"accept": "application/json; version=2.4;"}
#    if token:
#        http_headers =["authorization"] = Token {}".format(token)
#
#    response = requests.get(url, headers=http_headers, verify=False)
#    response = response.json()

response = requests.get(url, headers=http_headers, verify=False)
response = response.status_code
print()
print()
print('=' * 40)
print('response.status.code')
pprint(response)
print()


response = requests.get(url, headers=http_headers, verify=False)
response = response.text
print()
print()
print('=' * 40)
print('response.text')
pprint(response)
print()

response = requests.get(url, headers=http_headers, verify=False)
response = response.json()
print()
print()
print('=' * 40)
print('response.json()')
pprint(response)
print()

response = requests.get(url, headers=http_headers, verify=False)
response = response.headers
print()
print()
print('=' * 40)
print('response.headers')
pprint(response)
print()

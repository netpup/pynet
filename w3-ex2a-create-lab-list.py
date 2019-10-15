# import re
from pprint import pprint

'''
none of this is working.  try again later
def device_type_f(raw_device):
    if re.search(r"IOS-XE",raw_device) == True:
        device_type = 'cisco_ios'
    if re.search(r"vEOS",raw_device) == True:
        device_type = 'arista'
    if re.search(r"SRX",raw_device) == True:
        device_type = 'juniper'
    if re.search(r"Nx-OSv",raw_device) == True:
        device_type = 'cisco_nxos'
    return(device_type)

device_type = device_type_f('IOS-XE')
print(device_type)
'''

with open("lab_device_raw_list.txt") as f:
    output = f.read()

device_list = []
line = ''
output = output.splitlines()

for line in output:
    output.pop(0)
    hostname = output[0]
    hostname = hostname.split()
    hostname = hostname[0]

    output.pop(0)
    fqdn = output[0]
    fqdn = fqdn.split()
    fqdn = fqdn[2]

    output.pop(0)
    output.pop(0)
    output.pop(0)
    username = output[0]
    username = username.split()
    username = username[2]

    output.pop(0)
    password = output[0]
    password = password.split()
    password = password[2]
    output.pop(0)

    device_dict = {
        'hostname': hostname,
        'fqdn': fqdn,
        'username': username,
        'password': password
    }

    device_list.append(device_dict) 

pprint(device_list)

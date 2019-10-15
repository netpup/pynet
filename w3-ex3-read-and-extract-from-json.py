import json
import re
from pprint import pprint

filename_in = 'nxos_interfaces.json'
with open(filename_in) as f:
    data = json.load(f)
#print(data)

ipv4_list = []
ipv6_list = []

for intf_name, intf_value in data.items(): 
    if re.search(r"ipv4",str(intf_value)): 
        ip_addr = intf_value['ipv4']
        for ipv4_addr in ip_addr:
            ipv4_addr = ipv4_addr
            prefix_dict = ip_addr[ipv4_addr]
            prefix_length = prefix_dict['prefix_length']
            dict_add = {
                'ipv4_addr':ipv4_addr,
                'prefix_length': prefix_length
            }
            ipv4_list.append(dict_add)

    if re.search(r"ipv6", str(intf_value)): 
        ip_addr = intf_value['ipv6']
        for ipv6_addr in ip_addr:
            ipv6_addr = ipv6_addr
            prefix_dict = ip_addr[ipv6_addr]
            prefix_length = prefix_dict['prefix_length']
            dict_add = {
                'ipv6_addr':ipv6_addr,
                'prefix_length': prefix_length
            }
            ipv6_list.append(dict_add)

#pprint('=' * 60)
#pprint(ipv4_list)

#pprint('=' * 60)
#pprint(ipv6_list)
print('=' * 34)
print("{:<26}{:<8}".format('IPv4 addresses', 'Prefix'))
for ip_dict in ipv4_list:
    address = ip_dict['ipv4_addr']
    prefix = ip_dict['prefix_length']
    print("{:<26}{:<8}".format(address, prefix))
print('=' * 34)
print()
print()

print('=' * 68)
print("{:<60}{:<8}".format('IPv4 addresses', 'Prefix'))
for ip_dict in ipv6_list:
    address = ip_dict['ipv6_addr']
    prefix = ip_dict['prefix_length']
    print("{:<60}{:<8}".format(address, prefix))
print('=' * 68)


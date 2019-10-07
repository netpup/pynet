from netmiko import Netmiko
#from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios',
}

net_connect = Netmiko(**device1)

output = net_connect.send_command('show version', use_textfsm=True)

print(output)

output = net_connect.send_command('show lldp neighbor', use_textfsm=True)

print(output)

lldp_dict = output[0]

neighbor_int = lldp_dict['neighbor_interface']

print('=' * 50)
print('=' * 50)
print('Neighbor Interface is: ', neighbor_int)


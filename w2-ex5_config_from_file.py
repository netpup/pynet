from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

device1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

device2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

device_list = (device1, device2)

for device in device_list:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_from_file(config_file = 'vlan_config.txt')
    print(output)
    net_connect.save_config()
    net_connect.disconnect()



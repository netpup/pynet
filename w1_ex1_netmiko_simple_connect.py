from netmiko import Netmiko
from getpass import getpass


password = getpass()

net_conn = Netmiko(host = 'nxos1.lasthop.io', username = 'pyclass', password=password, device_type='cisco_nxos')
print(net_conn.find_prompt())

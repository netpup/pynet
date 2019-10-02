from netmiko import Netmiko
from getpass import getpass

password = getpass()

host1 ='cisco3.lasthop.io'

device1 = {
    'host' : host1,
    'username' : 'pyclass', 
    'password': password,
    'device_type' : 'cisco_ios'
}

net_connect = Netmiko(**device1)
output = net_connect.send_command('show version')

filename = host1 + '_show_version.txt'

f = open(filename, mode = 'w')
f.write(output)
f.flush

#print to screen
print('complete')

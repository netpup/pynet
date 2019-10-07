from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

device1 = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios',
}

fast_device1 = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios',
    'fast_cli': True
}


cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup'
]

#  without fast cli
net_connect = Netmiko(**device1)

start_time = datetime.now()
output = net_connect.send_config_set(cfg)
end_time = datetime.now()

execution_time = end_time - start_time

print(output)

print('\n')
print('execution time was:', execution_time)

net_connect.disconnect()


# with fast cli
net_connect = Netmiko(**fast_device1)

start_time = datetime.now()
output = net_connect.send_config_set(cfg)
end_time = datetime.now()

execution_time = end_time - start_time

print(output)

print('\n')
print('execution time was:', execution_time)
print('\n')

net_connect.disconnect()

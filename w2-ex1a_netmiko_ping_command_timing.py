from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command_timing('ping', strip_prompt=False, strip_command=False)
print(output)

#protocol
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

#target address
output = net_connect.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
print(output)

#repeat count
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

#datagram size
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

#timeout
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

#extended
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

#sweep range of sizes
output = net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)

net_connect.disconnect()

'''  Teacher way to do it.  using output += .  looks better
net_connect = ConnectHandler(**device1)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(output)
print()
'''

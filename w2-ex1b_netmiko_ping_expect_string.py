from netmiko import Netmiko
#from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios'
}

net_connect = Netmiko(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command('ping', expect_string=r'ip', strip_prompt=False, strip_command=False)

#protocol
output += net_connect.send_command('\n', expect_string=r'address', strip_prompt=False, strip_command=False)

#target address
output += net_connect.send_command('8.8.8.8', expect_string=r'5', strip_prompt=False, strip_command=False)

#repeat count
output += net_connect.send_command('\n', expect_string=r'100', strip_prompt=False, strip_command=False)

#datagram size
output += net_connect.send_command('\n', expect_string=r'2', strip_prompt=False, strip_command=False)

#timeout
output += net_connect.send_command('\n', expect_string=r'n', strip_prompt=False, strip_command=False)

#extended
output += net_connect.send_command('\n', expect_string=r'n', strip_prompt=False, strip_command=False)

#sweep range of sizes
output += net_connect.send_command('\n', expect_string=r'', strip_prompt=False, strip_command=False)

net_connect.disconnect()

print(output)

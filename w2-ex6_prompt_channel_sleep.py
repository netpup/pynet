from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import time

password = getpass()

device1 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
    'session_log': 'my_output.txt',
}


net_connect = Netmiko(**device1)

output = net_connect.find_prompt()
print('exercise 6a:find_prompt\n',output)

net_connect.config_mode()
output = net_connect.find_prompt()
print('exercise 6b:config mode find_prompt\n',output)

net_connect.exit_config_mode()
output = net_connect.find_prompt()
print('exercise 6c:exit config mode find_prompt\n',output)

net_connect.write_channel('disable\n')
#output = net_connect.find_prompt()
print('exercise 6d&e:disable with write_channel-read_channel \n')
time.sleep(2)
print(net_connect.read_channel())
#print('exercise 6e:time.sleep2-read_channel \n',output)

net_connect.enable()
output = net_connect.find_prompt()
print('exercise 6f:enable method find_prompt\n',output)


#net_connect.save_config()
#net_connect.disconnect()



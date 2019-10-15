from netmiko import Netmiko
import yaml

yaml_filename = '/home/netpup/.netmiko.yml'

with open(yaml_filename) as f:
    data = yaml.load(f)

device = data['cisco3']

net_connection = Netmiko(**device)  
print(net_connection.find_prompt()) 


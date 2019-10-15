from netmiko import Netmiko
from ciscoconfparse import CiscoConfParse

# define parameters

output_filename = 'cisco-sho-run.txt'


###################################################
# import yaml device list and pick device
import yaml

yaml_filename = '/home/netpup/.netmiko.yml'

with open(yaml_filename) as f:
    data = yaml.load(f)
    
device = data['cisco4'] 
###################################################


#main code

net_connect = Netmiko(**device)

output = net_connect.send_command('sho run', use_textfsm=True)

with open(output_filename, 'wt') as f:
    f.write(output)

cisco_obj = CiscoConfParse("cisco-sho-run.txt")

print()
for ip_addr in cisco_obj.find_objects(r"^\sip address"):
    print("Interface Line: ", ip_addr.parent.text) 
    print("IP Address Line: ", ip_addr.text) 

print()

'''
#the teacher's code
interface = cisco_obj.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
)

for intf in interface:
    print('Interface Line: ',intf.text)
    ip_addr = intf.re_search_children(r"ip address")[0].text
    print('IP Address Line:', ip_addr)
'''

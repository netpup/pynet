from pprint import pprint

arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""
arp_split= arp_data.splitlines()
#remove blank and first line
arp_split.pop(0)
arp_split.pop(0)

arp_list = []

for arp_line in arp_split:
    line = arp_line.split()
    ip_addr = line[1]
    mac_addr = line[3]
    interface = line[5]
    arp_dict = {'ip_addr': ip_addr, 'mac_addr': mac_addr, 'interface': interface }
    arp_list.append(arp_dict)

pprint(arp_list)


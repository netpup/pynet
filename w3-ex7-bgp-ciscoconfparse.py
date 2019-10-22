from netmiko import Netmiko
from ciscoconfparse import CiscoConfParse

# define parameters

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""




#main code

# have to splitlines when not reading from a config files
cisco_obj = CiscoConfParse(bgp_config.splitlines())


bgp_peers = []


bgp_peers = []
neighbors = cisco_obj.find_objects_w_parents(
    parentspec=r"router bgp", childspec=r"neighbor"
)

for neighbor in neighbors:
    _, neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))

print('')
print('tulpe format')
print(bgp_peers)

print('')
print("{:<20}{:>10}".format('Neighbor IP', 'Remote-AS'))

for peer in bgp_peers:
    print("{:<20}{:>10}".format(peer[0], peer[1]))

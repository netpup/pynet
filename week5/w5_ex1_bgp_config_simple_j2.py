
from jinja2 import Template

Bgp_Var = {
    'local_as' : 10,
    'peer1_ip': '10.1.20.2',
    'peer1_as': 20,
    'peer2_ip': '10.1.30.2',
    'peer2_as': 30
}


bgp_template = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }}  remote-as {{ peer2_as }}
"""

J2_template = Template(bgp_template)
output = J2_template.render(**Bgp_Var)
print('-' * 20)
print(output)
print('-' * 20)


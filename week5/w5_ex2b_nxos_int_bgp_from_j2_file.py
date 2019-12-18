
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

# create dictionary and device list
nxos1 = {
    'interface_num': 'Ethernet1/1',
    'interface_ip': '10.1.100.1',
    'interface_mask': '24',
    'as_num': '22',
    'peer_ip': '10.1.100.2',
}
nxos2 = {
    'interface_num': 'Ethernet1/1',
    'interface_ip': '10.1.100.2',
    'interface_mask': '24',
    'as_num': '22',
    'peer_ip': '10.1.100.1',
}

device_list = [nxos1, nxos2]

print('-' * 20)
# render template
for device in device_list:
  template_file = "w5_ex2b-nxos_int_bgp.j2"
  template = env.get_template(template_file)
  output = template.render(**device)
  print(output)
  print('')
  print('')

print('-' * 20)

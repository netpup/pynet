
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2



env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")



#device_list = [nxos1, nxos2]

#print('-' * 20)
## render template
#for device in device_list:
#  template_file = "w5_ex2b-nxos_int_bgp.j2"
#  template = env.get_template(template_file)
#  output = template.render(**device)
#  print(output)
#  print('')
#  print('')
#
#print('-' * 20)

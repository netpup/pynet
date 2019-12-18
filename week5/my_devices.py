from getpass import getpass
 
password = getpass()


nxos1  = {
    'hostname':  'nxos1.lasthop.io',
    'device_type': 'cisco_nxos',
    'ssh_port': 22,
    'nxapi_port': 8443,
    'username': 'pyclass',
    'password': password
}
nxos2 = {
    'hostname': 'nxos2.lasthop.io',
    'device_type': 'cisco_nxos',
    'ssh_port': 22,
    'nxapi_port': 8443,
    'username': 'pyclass',
    'password': password
}

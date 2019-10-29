import textfsm
from pprint import pprint

template_file = 'w4-ex2-textfsm-sho-int-status_expand.tpl'
template = open(template_file)

with open('ex2_show_int_status.txt') as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close


int_list = []
int_dict = {}


for item in data: 
    int_dict = { 
        'PORT_NAME': item[0],
        'STATUS': item[1], 
        'VLAN': item[2], 
        'SPEED': item[3], 
        'DUPLEX': item[4], 
        'PORT_TYPE': item[5] 
    } 
    int_list.append(int_dict)

pprint(int_list)
    

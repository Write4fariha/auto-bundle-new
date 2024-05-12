import json

# CONVERT JSON DATA TO PYTHON DATA
jsonfile=open("config_data.json")

sw_config_data=json.load(jsonfile)
# print(sw_config_data)

sw_config_data = {
    "intf":"gig0/1",
    "desc":"connected to server",
    "intf_mode":"access",
    "vlan_id":"10"
}

# # CONVERT PYTHON DATA TO JSON DATA
jsonlfile=open("jsonconfig_data.json",'w')
output=json.dump(sw_config_data,jsonlfile)

sw_config_syntax = {
    "intf":"interface {}",
    "desc":"description {}",
    "intf_mode":"switchport mode {}",
    "vlan_id":"switchport mode access {}"
}

for k,v in sw_config_data.items():
    print(sw_config_syntax [k].format(v))

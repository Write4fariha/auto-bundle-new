
import yaml

# CONVERT YAML DATA TO PYTHON DATA

yamlfile=open("config_data.yaml")

sw_config_data=yaml.safe_load(yamlfile)
# print(sw_config_data)

# sw_config_data = {
#     "intf":"gig0/1",
#     "desc":"connected to server",
#     "intf_mode":"access",
#     "vlan_id":"10"
# }

sw_config_syntax = {
    "intf":"interface {}",
    "desc":"description {}",
    "intf_mode":"switchport mode {}",
    "vlan_id":"switchport mode access {}"
}


# print(sw_config_syntax ["intf"].format(sw_config_data["intf"]))
for k,v in sw_config_data.items():
    print(sw_config_syntax [k].format(v))

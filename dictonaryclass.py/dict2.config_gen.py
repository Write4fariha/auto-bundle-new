# sw_config_data = {
#     "intf":"gig0/1",
#     "desc":"connected to server",
#     "intf_mode":"access",
#     "vlan_id":"10"
# }

# sw_config_syntax = {
#     "intf":"interface {}",
#     "desc":"description {}",
#     "intf_mode":"switchport mode {}",
#     "vlan_id":"switchport mode access {}"
# }
# # print(sw_config_data)
# # print(sw_config_syntax)

# # print(sw_config_syntax ["intf"].format(sw_config_data["intf"]))
# for k,v in sw_config_data.items():
#     print(sw_config_syntax [k].format(v))


#Config for dictionary under list and using for loop for list and dict

sw_config_list = [{
    "intf":"gig0/1",
    "desc":"connected to server1",
    "intf_mode":"access1",
    "vlan_id":"10"
},
{
    "intf":"gig0/2",
    "desc":"connected to server2",
    "intf_mode":"access2",
    "vlan_id":"20"
},
{
    "intf":"gig0/3",
    "desc":"connected to server3",
    "intf_mode":"access3",
    "vlan_id":"30"
}]

sw_config_syntax = {
    "intf":"interface {}",
    "desc":"description {}",
    "intf_mode":"switchport mode {}",
    "vlan_id":"switchport mode access {}"
}
# print(sw_config_data)
# print(sw_config_syntax)

# print(sw_config_syntax ["intf"].format(sw_config_data["intf"]))

for sw_config_data in sw_config_list:
    print(sw_config_data)
    # for k,v in sw_config_data.items():
        # print(sw_config_syntax [k].format(v))

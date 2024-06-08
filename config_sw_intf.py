import os
import yaml
from netmiko import ConnectHandler

# # # import jinja2 --it will import complete jinja2 template

# below is another method to import only required object from jinja2 template
from jinja2 import FileSystemLoader,Environment

# load yaml file into data and convert it into python format

file=open("config_data_sw_intf.yml","r")
data=yaml.safe_load(file)
# print(data)

file=open("inv.yml","r")
devices=yaml.safe_load(file)
# print(device)

# load jinja2 template from file 

template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("config_jinja_sw_intf.j2")

# Render the template with the data
# data = ""
rendered_output = template.render(config_data=data) 
# print(rendered_output) # Print rendered output
config_list=rendered_output.splitlines()

# opening new file and writting rendered output value in it. It will create new file and dislay the output on it.
# config_file=open("config_gen_vlan.data","w")
# config_file.write(rendered_output)
# config_file.close()


# # it will open existing file created above and read all lines from that file and print the output 
# config_file=open("config_gen_vlan.data","r")
# config_list=config_file.readlines()
# # print(config_list)

# Retrieve the value of an environment variable

user = os.getenv('USERNAME')
user_password = os.getenv('PASSWORD')

# # Connect to multiple devices

for device in devices:
    print("Connected to the device",device["hostname"])
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username= user,password= user_password)

# # Example command: display the vlan & Netmiko different module uses

    # output = net_connect.send_command("sh vlan bri") # this command use to display the mention command output
    output = net_connect.send_config_set(config_list) # config_set make config changes on switches with data mentioned in config_list file location
    # output = net_connect.send_config_from_file("config_gen_vlan.data") #config_from_file make config changes on switches with  data by passing direct file name itself
    print("Configuration PUSHED")
    print(output)

# Disconnect from the device
    net_connect.disconnect()
    print("Disconnect the device.\n")


# # Connect to the device

# net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username= 'netg',password= 'india')
# print("Connected to the device.")

# # Example command: display the running configuration

# output = net_connect.send_command("sh vlan bri")
# output = net_connect.send_config_set(config_list)
# # output = net_connect.send_config_from_file("config_gen_vlan.data") 
# print("Configuration PUSHED with keeping inventory data outside the code")
# print(output)

# # Disconnect from the device
# net_connect.disconnect()
# print("Disconnect the device.")

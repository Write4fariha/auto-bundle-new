
import yaml
from netmiko import ConnectHandler
# # import jinja2 --it will import complete jinja2 template

# # below is another method to import only required object from jinja2 template
# from jinja2 import FileSystemLoader,Environment

# # load yaml file into data and convert it into python format
# file=open("config_data.yml","r")
# data=yaml.safe_load(file)
# # print(data)

# # load jinja2 template from file 

# template_loader = FileSystemLoader(searchpath=".")
# env = Environment(loader=template_loader)
# template = env.get_template("config_jinja.j2")

# # Render the template with the data

# rendered_output = template.render(config_vlan=data) 

# # Pirnt rendered output
# # print(rendered_output)

# # opening new file and writting rendered output value in it. It will create new file and dislay the output on it.
# config_file=open("config_gen.data","w")
# config_file.write(rendered_output)
# config_file.close()


# # it will open existing file created above and read all lines from that file and print the output 
# config_file=open("config_gen.data","r")
# config_list=config_file.readlines()
# print(config_list)



# Device information
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.64.5',  # IP address of the device
    'username': 'netg',    # Username
    'password': 'netg',  # Prompt for password securely
    # 'secret': getpass('Enter enable secret: '),      # Prompt for enable secret securely, if needed
}


# Connect to the device
net_connect = ConnectHandler(**device)
print("Connected to the device.")

# Example command: display the running configuration
output = net_connect.send_command("show running config")
print("Running Config")

# Disconnect from the device
net_connect.disconnect()
print("Disconnect the device.")
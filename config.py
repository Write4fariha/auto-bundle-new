
import yaml
# import jinja2 --it will import complete jinja2 template

# below is another method to import only required object from jinja2 template

from jinja2 import FileSystemLoader,Environment

# load yaml file into data and convert it into python format
file=open("config_data.yml","r")
data=yaml.safe_load(file)
# print(data)

# load jinja2 template from file 

template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("config_jinja.j2")

# Render the template with the data

rendered_output = template.render(config_vlan=data) 

# Pirnt rendered output
print(rendered_output)
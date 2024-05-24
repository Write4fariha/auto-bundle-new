
import yaml
import jinja2

file=open("config_data.yml","r")
config_vlan=yaml.safe_load(file)
print(config_vlan)

# load jinja2 template from file 

template_loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=template_loader)
template = env.get_template("config_jinja.j2")

# Render the template with the data

rendered_output = template.render(config_vlan=config_vlan)

# Pirnt rendered output
print(rendered_output)
# python file

vlan_config=open("vlan.txt",'w')

for item in range(0,7):
    # print(f"vlan {item}\n")
    vlan_config.write(f"vlan {item}\n")

vlan_config.close()

read_vlan_config=open("vlan.txt",'r')
# read_file=read_vlan_config.read()
# read_file=read_vlan_config.readline()

for item in range(0,7):
    read_file=read_vlan_config.readline()
    # read_file1=read_vlan_config.readline()
    # read_file2=read_vlan_config.readline()
    print(read_file)
# print(read_file1)
# print(read_file2)
# for item in read_file:
#     print(item)
# print(read_vlan_config.read())

read_vlan_config.close()

#
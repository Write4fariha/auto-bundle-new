ip=input("Enter your ip:")
print("Given IP:" + ip)
if ip.startswith("10."):
    print("Class A private IP")
elif ip.startswith("172.16."):
    print("class B Private IP")
elif ip.startswith("192.168."):
    print("Class C private IP")
else:
    print("Not any Private Class")
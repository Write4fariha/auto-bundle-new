ip="222.255.11.4"

if ip.startswith("1.") or float(ip[:4]) <= 127:
    print("class A public IP")
elif ip.startswith("128.") and (float(ip[4:5]) >= 0. and float(ip[4:8]) <= 255.):
    print("class B Public IP")
elif ip.startswith("192.") or float(ip[:4]) <= 223:
    print("class C public IP")
else:
    print("Given Ip is not Private IP")

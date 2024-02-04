# deviceinfo={
#     "name":"CISCO-Device",
#     "Device":"Router",
#     "numbers":4,
#     "Users_info":[{"name":"fariha","profile":"SSRE"},{"name":"khan","profile":"network eng"}]
# }
# #print(deviceinfo["Users_info"][0]["profile"])
# print(list(deviceinfo["Users_info"][0].values())[1])

Device_Details = [{"switch":"Meraki"},{"router":"cisco"}]

# for item in Device_Details:
#     for k,v in item.items():
#         print((k,v))

t1=[(k,v) for item in Device_Details for k,v in item.items()]
print(t1)





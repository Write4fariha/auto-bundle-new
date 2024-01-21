deviceinfo={
    "name":"CISCO-Device",
    "Device":"Router",
    "numbers":4,
    "Users_info":[{"name":"fariha","profile":"SSRE"},{"name":"khan","profile":"network eng"}]
}
#print(deviceinfo["Users_info"][0]["profile"])
print(list(deviceinfo["Users_info"][0].values())[1])



import requests
import json
import OpenSSL.SSL

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class VManageAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.verify = False  # Disable SSL verification for simplicity
        self.username = username
        self.password = password
        self._authenticate()

    def _authenticate(self):
        login_url = f"{self.base_url}/j_security_check"
        login_data = {
            "j_username": self.username,
            "j_password": self.password
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = self.session.post(login_url, data=login_data, headers=headers)
        if response.status_code != 200 or "html" in response.text:
            raise Exception("Failed to authenticate with vManage")

    def get_device_information(self):
        device_url = f"{self.base_url}/dataservice/device"
        response = self.session.get(device_url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve device information: {response.text}")
        return response.json()

if __name__ == "__main__":
    # Define vManage details
    vmanage_info = {
        "base_url": "https://10.10.20.90:443",  # e.g., https://192.168.1.1:8443
        "username": "admin",
        "password": "C1sco12345"
    }

    # Initialize API client
    vmanage_api = VManageAPI(vmanage_info["base_url"], vmanage_info["username"], vmanage_info["password"])

    # Get device information
    try:
        device_info = vmanage_api.get_device_information()
        print("Device Information:\n")
        print(json.dumps(device_info, indent=4))
    except Exception as e:
        print(f"Failed to retrieve device information. Error: {e}")
# 
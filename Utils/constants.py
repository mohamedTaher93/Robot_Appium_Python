import json
import os

appium_server_url = 'http://127.0.0.1:4723'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
capabilities_path = f"{ROOT_DIR}/capabilities.json"

def get_appium_capabilities():
    with open(capabilities_path, 'r') as c:
        return json.load(c)

def get_appium_capability(capability_key: str):
    with open(capabilities_path, 'r') as c:
        capabilities = json.load(c)
        return capabilities[capability_key]

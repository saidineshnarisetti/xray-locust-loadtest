import requests
from config import BASE_URL, AUTH_HEADER
import json
import utils
from utils.helpers import GeneratedNames
from utils.locust_wrappers import tracked_request
GeneratedNames.__init__

def create_watch(watch_name: str, description: str, active: bool,
                    resources: list, assigned_policies: list) -> dict | None:
    url = f"{BASE_URL}/xray/api/v2/watches"
    headers = {**AUTH_HEADER, 'Content-Type': 'application/json'}

    payload = {
        "general_data": {
            "name": watch_name,
            "description": description,
            "active": active
        },
        "project_resources": {
            "resources": resources
        },
        "assigned_policies": assigned_policies
    }
    response = tracked_request("create_watch","POST", url, headers=AUTH_HEADER,json=payload)
    print(f"[CREATE WATCH] Status: {response.status_code}, Response: {response.text}")      

    if response.status_code in [200, 201]:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("[CREATE WATCH] Error decoding JSON response.")
    else:
         raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")


def run_create_watch(names):
    watch_name = names.WATCH_NAME
    description = "This is an example watch #1"
    active = True
    resources = [
        {
            "type": "repository",
            "bin_mgr_id": "default",
            "name": "docker-local",
            "filters": [
                {
                    "type": "regex",
                    "value": ".*"
                }
            ]
        }
    ]
    assigned_policies = [
        {
            "name": names.POLICY_NAME,
            "type": "security"
        }
    ]

    result = create_watch(watch_name, description, active, resources, assigned_policies)

    if result:
        print("[CREATE WATCH] Watch created successfully:", result)
    else:
        print("[CREATE WATCH] Failed to create watch.")

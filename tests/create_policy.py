import requests
from config import BASE_URL, AUTH_HEADER
import json
from utils.helpers import GeneratedNames
from utils.locust_wrappers import tracked_request

def create_policy(policy_name, description, rules):
    url = f"{BASE_URL}/xray/api/v2/policies"
    payload = {
        "name": policy_name,
        "description": description,
        "type": "security",
        "rules": rules
    }
    response = tracked_request("create_policy","POST", url, headers=AUTH_HEADER,json=payload)

    print(f"[CREATE POLICY] Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200 or response.status_code == 201:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("[CREATE POLICY] Error decoding JSON response.")
    else:
        raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")

def run_create_policy(names):

    policy_name = names.POLICY_NAME
    description = "This is a specific CVEs security policy"
    rules = [
        {
            "name": "some_rule",
            "priority": 1,
            "criteria": {
                "malicious_package": False,
                "fix_version_dependant": False,
                "min_severity": "high"
            },
            "actions": {
                "mails": [],
                "webhooks": [],
                "fail_build": False,
                "block_release_bundle_distribution": False,
                "block_release_bundle_promotion": False,
                "notify_deployer": False,
                "notify_watch_recipients": False,
                "create_ticket_enabled": False,
                "block_download": {
                    "active": False,
                    "admin_override": False
                }
            }
        }
    ]
    create_policy(policy_name, description, rules)
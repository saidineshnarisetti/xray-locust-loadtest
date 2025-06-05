import requests
from config import BASE_URL, AUTH_HEADER
from utils.locust_wrappers import tracked_request

def get_violations(repo, path):
    payload = {
        "filters": {
            "watch_name": "Security_watch_1",
            "violation_type": "Security",
            "min_severity": "High",
            "resources": {
                "artifacts": [{"repo": repo, "path": path}]
            }
        },
        "pagination": {"order_by": "created", "direction": "asc", "limit": 100, "offset": 1}
    }

    url = f"{BASE_URL}/xray/api/v1/violations"
    response = tracked_request("get_violations","POST", url, headers=AUTH_HEADER,json=payload)
    print(f"[VIOLATIONS] Status: {response.status_code}, Response: {response.text}")
    if response.status_code not in [200] :
        raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")
    


def run_get_violations():
    get_violations("docker-local", "/alpine/3.9/manifest.json")

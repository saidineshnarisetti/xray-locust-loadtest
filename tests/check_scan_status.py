import requests
from config import BASE_URL, AUTH_HEADER
import json

def check_scan_status(repo_key, artifact_path):
    url = f"{BASE_URL}/xray/api/v1/artifact/status"
    payload = {
        "repo": repo_key,
        "path": artifact_path
    }
    response = requests.post(url, headers=AUTH_HEADER, json=payload)

    print(f"[SCAN STATUS] Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        try:
            status_data = response.json()
            return status_data
        except json.JSONDecodeError:
            print("[SCAN STATUS] Error decoding JSON response.")
            return None
    else:
        return None

if __name__ == "__main__":
    check_scan_status("docker-local", "/alpine/3.9/manifest.json")
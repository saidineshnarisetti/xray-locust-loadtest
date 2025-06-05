import requests
from config import BASE_URL, AUTH_HEADER

def check_scan_status(repo, path):
    payload = {
        "repo": repo,
        "path": path
    }

    url = f"{BASE_URL}/xray/api/v1/artifact/status"
    response = requests.post(url, headers=AUTH_HEADER, json=payload)
    print(f"[SCAN STATUS] Status: {response.status_code}, Response: {response.text}")

def run_check_scan_status():
    check_scan_status("docker-local", "/alpine/3.9/manifest.json")

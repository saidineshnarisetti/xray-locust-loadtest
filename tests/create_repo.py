import requests
from config import BASE_URL, AUTH_HEADER
from utils.helpers import GeneratedNames
from utils.locust_wrappers import tracked_request

def create_repository(repo_key):
    payload = {
        "key": repo_key,
        "packageType": "docker",
        "rclass": "local",
        "xrayIndex": True
    }

    url = f"{BASE_URL}/artifactory/api/repositories/{repo_key}"

    response = tracked_request("create_repo", "PUT", url, headers=AUTH_HEADER, json=payload)
    print(f"[CREATE REPO] Status: {response.status_code}")        

    if response.status_code == 400 or response.status_code == 201 and "already exists" in response.text:
        print(f"[CREATE REPO] Repository '{repo_key}' already exists. Skipping.")
    else:
        raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")


def run_create_repository():
    create_repository("docker-local")

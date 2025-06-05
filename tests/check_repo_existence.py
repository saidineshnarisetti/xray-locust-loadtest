import requests
from config import BASE_URL, AUTH_HEADER
import json
from utils.locust_wrappers import tracked_request

def check_repository_existence(repo_key):
    url = f"{BASE_URL}/artifactory/api/repositories"
    #response = requests.get(url, headers=AUTH_HEADER)
    response = tracked_request("check_repository_existence","GET", url, headers=AUTH_HEADER)        
    
    if response.status_code == 200:
        repositories = response.json()
        exists = any(repo['key'] == repo_key for repo in repositories)
        if exists:
            print(f"[CHECK REPO] Repository '{repo_key}' exists.")
            return True
        else:
            print(f"[CHECK REPO] Repository '{repo_key}' does not exist.")
            return False
    else:
        raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")
        return False

def run_check_repository_existence():
    check_repository_existence("docker-local")
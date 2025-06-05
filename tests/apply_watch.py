import requests
from config import BASE_URL, AUTH_HEADER
import json
import utils
from utils.helpers import GeneratedNames
from utils.locust_wrappers import tracked_request

def apply_watch(watch_names, start_date, end_date):
    url = f"{BASE_URL}/xray/api/v1/applyWatch"
    headers = AUTH_HEADER
    headers["Content-Type"] = "application/json"

    payload = {
        "watch_names": watch_names,
        "date_range": {
            "start_date": start_date,
            "end_date": end_date
        }
    }

    response = tracked_request("apply_watch","POST", url, headers=AUTH_HEADER,json=payload)
    print(f"[APPLY WATCH] Status: {response.status_code}, Response: {response.text}")
 
    if response.status_code in [200, 202]:
        return response.json() if response.content else {"info": "History Scan is in progress"}
    else:
        raise Exception(f"[ERROR] Failed to create repo: {response.status_code} - {response.text}")

def run_apply_watch(names):
    watch_names = [f"{names.WATCH_NAME}"]
    start_date = "2025-04-07T10:25:00+02:00"
    end_date = "2025-04-07T10:30:00+02:00"

    result = apply_watch(watch_names, start_date, end_date)

    if result:
        print("[SUCCESS] Watch applied:", result)
    else:
        print("[ERROR] Failed to apply watch.")

# utils/locust_wrappers.py
import time
import requests
from locust import events

def tracked_request(name, method, url, **kwargs):
    start_time = time.time()
    try:
        response = requests.request(method, url, **kwargs)
        duration = int((time.time() - start_time) * 1000)
        events.request.fire(
            request_type=method,
            name=name,
            response_time=duration,
            response_length=len(response.content),
            exception=None
        )
        return response
    
    except Exception as e:
        duration = int((time.time() - start_time) * 1000)
        events.request.fire(
            request_type=method,
            name=name,
            response_time=duration,
            response_length=0,
            exception=e
        )
        raise

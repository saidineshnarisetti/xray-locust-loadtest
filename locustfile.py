from locust import HttpUser, between
from core.tasks import FullScanWorkflow

class JFrogUser(HttpUser):
    wait_time = between(1, 3)
    tasks = {FullScanWorkflow: 1}
    host="https://trialf6dxqy.jfrog.io"
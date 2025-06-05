from locust import task, TaskSet
from utils.helpers import GeneratedNames
from tests import (
    check_repo_existence,
    create_policy,
    create_repo,
    create_watch,
    apply_watch,
    violations
)

class FullScanWorkflow(TaskSet):
    def on_start(self):
        self.repo_key = "docker-local"
        self.image_path = "/alpine/3.9/manifest.json"

    @task()
    def run_full_scan(self):
        print("[RUNNING] Full scan workflow via tests")
        self.names = GeneratedNames()
        create_repo.run_create_repository()
        check_repo_existence.run_check_repository_existence()
        create_policy.run_create_policy(self.names)
        create_watch.run_create_watch(self.names)
        apply_watch.run_apply_watch(self.names)
        violations.run_get_violations()

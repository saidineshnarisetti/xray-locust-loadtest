import json
from config import AUTH_HEADER
import uuid
import os

class GeneratedNames:
    def __init__(self):
        self.WATCH_NAME = f"watch_{uuid.uuid4().hex[:8]}"
        self.POLICY_NAME = f"policy_{uuid.uuid4().hex[:8]}"
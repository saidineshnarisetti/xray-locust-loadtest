# BASE_URL = "https://trialf6dxqy.jfrog.io"
# AUTH_HEADER = {
#     "Authorization": "Basic c2VjdXJlUGFzc3dvcmQxMjM=",
#     "Content-Type": "application/json"
# }

import base64

username = "admin-perf"
password = "securePassword123"

creds = f"{username}:{password}"
encoded = base64.b64encode(creds.encode()).decode()

BASE_URL = "https://trialf6dxqy.jfrog.io"
AUTH_HEADER = {
    "Authorization": f"Basic {encoded}",
    "Content-Type": "application/json"
}

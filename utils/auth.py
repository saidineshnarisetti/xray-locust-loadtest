import base64

def encode_credentials(username, password):
    creds = f"{username}:{password}"
    return base64.b64encode(creds.encode()).decode()
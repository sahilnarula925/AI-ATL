import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/generative-language.retriever",
    "https://www.googleapis.com/auth/generative-language.tuning",
    "https://www.googleapis.com/auth/cloud-platform",
]


def load_creds(type):
    creds = None

    if os.path.exists(f"token_{type}.json"):
        creds = Credentials.from_authorized_user_file(f"token_{type}.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f"client_secret_{type}.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(f"token_{type}.json", "w") as token:
            token.write(creds.to_json())
    return creds

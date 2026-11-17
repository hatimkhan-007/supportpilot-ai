import os
from pathlib import Path
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials


BACKEND_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BACKEND_DIR / ".env")

service_account_path = os.getenv(
    "FIREBASE_SERVICE_ACCOUNT_PATH"
)

if not service_account_path:
    raise RuntimeError(
        "Firebase service account path is missing."
    )

credential_path = BACKEND_DIR / service_account_path

if not credential_path.is_file():
    raise FileNotFoundError(
        f"Firebase credentials not found: {credential_path}"
    )


if not firebase_admin._apps:
    cred = credentials.Certificate(
        str(credential_path)
    )

    firebase_admin.initialize_app(cred)

    print("Firebase Admin SDK initialized successfully.")

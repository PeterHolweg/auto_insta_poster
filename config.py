import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = Path(os.getenv("OUTPUT_FOLDER", BASE_DIR / "outputs"))
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Image provider
IMAGE_API_KEY = os.getenv("IMAGE_API_KEY")
IMAGE_API_ENDPOINT = os.getenv("IMAGE_API_ENDPOINT")
IMAGE_MODEL = os.getenv("IMAGE_MODEL")


# S3
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv("S3_REGION")
S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL") or None


# Instagram
IG_USER_ID = os.getenv("IG_USER_ID")
IG_LONG_LIVED_TOKEN = os.getenv("IG_LONG_LIVED_TOKEN")
FACEBOOK_APP_ID = os.getenv("FACEBOOK_APP_ID")
FACEBOOK_APP_SECRET = os.getenv("FACEBOOK_APP_SECRET")


# Other
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DAILY_POST_TIME = os.getenv("DAILY_POST_TIME", "09:00")

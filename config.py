import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')


def _as_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {'1', 'true', 'yes', 'on'}


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'change-this-development-key')
    RESUME_DIRECTORY = str(BASE_DIR / 'static' / 'resume')
    RESUME_FILENAME = 'resume.pdf'
    EMAIL_HOST = os.getenv('EMAIL_HOST', '')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
    EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', '')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', '')
    EMAIL_USE_SSL = _as_bool(os.getenv('EMAIL_USE_SSL'), False)
    EMAIL_USE_TLS = _as_bool(os.getenv('EMAIL_USE_TLS'), True)

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'change-this-development-key')
    RESUME_DIRECTORY = str(BASE_DIR / 'static' / 'resume')
    RESUME_FILENAME = 'resume.pdf'
    EMAIL_HOST = os.getenv('EMAIL_HOST', '')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
    EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', '')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', '')

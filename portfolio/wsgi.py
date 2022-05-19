import os
import pathlib

import dotenv

from portfolio.settings import BASE_DIR
from django.core.wsgi import get_wsgi_application

# CURRENT_DIR = pathlib.Path(__file__).resolve().parent
# BASE_DIR= CURRENT_DIR.parent
# ENV_FILE_PATH = BASE_DIR / ".env"

# dotenv.read_dotenv(str(ENV_FILE_PATH))

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

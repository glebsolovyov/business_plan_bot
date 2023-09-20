import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
CHAT_ID_FOR_MESSAGES = os.environ.get('CHAT_ID_FOR_MESSAGES')
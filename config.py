import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
admin = int(os.environ.get('ADMIN_ID'))
CHANNEL_NEWS_ID = os.environ.get('CHANNEL_ID')

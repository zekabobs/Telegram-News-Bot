import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
DB = os.path.join(os.getcwd(), 'db_news.db')
admin = int(os.environ.get('ADMIN_ID'))
CHANNEL_NEWS_ID = os.environ.get('CHANNEL_ID')

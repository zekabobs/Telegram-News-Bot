from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from loader import bot, dp
from config import CHANNEL_NEWS_ID, admin
from utils.parsing import to_parse


@dp.message_handler(Command(commands='send_news'))
async def send_news(message: Message):
    if message.from_user.id == admin:
        news = await to_parse()
        img = news['img']
        article = news['article']

        await bot.send_photo(CHANNEL_NEWS_ID, img, caption = article)
        await message.answer('Already send!')
    else:
        await message.answer('Permission denied')
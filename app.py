import logging
import os

from dotenv import load_dotenv, dotenv_values
from aiogram import Bot, Dispatcher, executor, types


envPath = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(envPath):
    load_dotenv(envPath)
    config = dotenv_values()
else:
    raise FileNotFoundError

bot = Bot(token=config['bot_token'])
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start_cmd(message: types.Message):
    await message.answer("Приветствую, я бот новостной рассылки. Узнай свежие новости города Ижевск первым.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
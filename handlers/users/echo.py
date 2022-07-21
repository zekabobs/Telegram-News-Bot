from aiogram.types import Message
from loader import dp


@dp.message_handler()
async def echo_send(message: Message):
    await message.reply('echo')
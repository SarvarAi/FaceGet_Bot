from data.loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Привет!')

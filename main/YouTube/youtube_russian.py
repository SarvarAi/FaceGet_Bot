from aiogram.types import Message, CallbackQuery

from data.loader import dp, bot


@dp.callback_query_handler(lambda call: 'ru' in call.data)
async def russian(call: CallbackQuery):
    ...

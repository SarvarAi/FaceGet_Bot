from data.loader import dp, bot
from aiogram.types import Message, CallbackQuery
from .buttons import language_btn, ru_choose_social_networks
from data.database import GettingInfoFromUsers, InsertInfoIntoUsers


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user_id = message.chat.id

    check_is_user_registrated = GettingInfoFromUsers().is_user_registrated(user_id)

    if not check_is_user_registrated:
        InsertInfoIntoUsers().inserting_new_unique_users(message)

    await message.answer('''🇷🇺Добро пожаловать в GetFace! выберите язык
🇺🇿GetFace-ga xush kelibsiz! Tilni tanlang''', reply_markup=language_btn())


@dp.callback_query_handler(lambda call: 'ru' in call.data)
async def russian(call: CallbackQuery):
    message_id = call.message.message_id
    chat_id = call.message.chat.id

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Выберите социальную сеть',
        reply_markup=ru_choose_social_networks())

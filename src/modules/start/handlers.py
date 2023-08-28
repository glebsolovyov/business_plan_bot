from aiogram import types, Dispatcher

from bot import bot
from modules.start import keyboards


async def start_keyboard(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Меню', reply_markup=keyboards.start_keyboard)

    await callback_query.answer()


def register_start_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_callback_query_handler(callback=start_keyboard, text='start_keyboard')

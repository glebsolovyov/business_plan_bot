from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot import bot
from core.keyboards import to_start_keyboard

from messages import main_messages


async def about_project(callback_query: types.CallbackQuery) -> None:
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/table.png', 'rb'),
                         caption=main_messages.MESSAGE_FOR_ABOUT_PROJECT,
                         reply_markup=to_start_keyboard)

    await callback_query.answer()


async def relevance(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_RELEVANCE,
                           reply_markup=to_start_keyboard)

    await callback_query.answer()


async def proposal(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_PROPOSAL,
                           reply_markup=to_start_keyboard)

    await callback_query.answer()


async def advantages(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_ADVANTAGES,
                           reply_markup=to_start_keyboard)

    await callback_query.answer()


async def commercialization(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_COMMERCIALIZATION,
                           reply_markup=to_start_keyboard)

    await callback_query.answer()


async def intellectual_property(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_INTELLECTUAL_PROPERTY,
                           reply_markup=to_start_keyboard)

    await callback_query.answer()


def register_main_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        {'callback': about_project, 'text': 'about_project'},
        {'callback': relevance, 'text': 'relevance'},
        {'callback': proposal, 'text': 'proposal'},
        {'callback': advantages, 'text': 'advantages'},
        {'callback': commercialization, 'text': 'commercialization'},
        {'callback': intellectual_property, 'text': 'intellectual_property'},
    ]

    for handler in callback_query_handlers:
            dispatcher.register_callback_query_handler(**handler)


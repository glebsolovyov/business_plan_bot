from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot import bot, dp
from config import CHAT_ID_FOR_MESSAGES
from core.keyboards import to_start_keyboard
from core.states import BuySubscription, BuyUSB
from messages import main_messages
from modules.buy_product import keyboards


async def buy_product(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=main_messages.MESSAGE_FOR_BUY_PRODUCT,
                           reply_markup=keyboards.but_tariff_keyboard)

    await callback_query.answer()


async def buy_subscription(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Введите свое имя")

    await BuySubscription.name.set()


async def get_name_for_subscription(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text="Отправьте свой контакт",
                           reply_markup=keyboards.get_contact)

    await state.update_data(name=message.text)
    await BuySubscription.next()


async def buy_usb(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Введите свое имя")

    await BuyUSB.name.set()

async def get_name_for_usb(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text="Отправьте свой контакт",
                           reply_markup=keyboards.get_contact)

    await state.update_data(name=message.text)
    await BuyUSB.next()


def register_buy_product_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        {'callback': buy_product, 'text': 'buy_product'},
        {'callback': buy_subscription, 'text': 'buy_subscription'},
        {'callback': buy_usb, 'text': 'buy_usb'},
    ]
    message_handlers = [
        {'callback': get_name_for_subscription, 'state': BuySubscription.name},
        {'callback': get_name_for_usb, 'state': BuyUSB.name},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

    for handler in message_handlers:
        dispatcher.register_message_handler(**handler)

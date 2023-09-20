from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from core.keyboards import to_start_button

buy_subscription = InlineKeyboardButton("✅ Купить подписку на месяц", callback_data="buy_subscription")
buy_usb = InlineKeyboardButton("✅ Купить флешку", callback_data="buy_usb")

but_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(buy_subscription, buy_usb, to_start_button)


get_contact = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Отправить свой контакт', request_contact=True))
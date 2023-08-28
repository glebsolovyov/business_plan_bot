from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

to_start_button = InlineKeyboardButton('✅ Назад', callback_data='start_keyboard')
to_start_keyboard = InlineKeyboardMarkup(row_width=1).add(to_start_button)

to_start1_button = InlineKeyboardButton('✅ Далее', callback_data='start_keyboard')
to_start1_keyboard = InlineKeyboardMarkup(row_width=1).add(to_start1_button)

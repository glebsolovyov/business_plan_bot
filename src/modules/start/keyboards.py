from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


about_project = InlineKeyboardButton('✅ О проекте', callback_data='about_project')
relevance = InlineKeyboardButton('✅ Почему это актуально', callback_data='relevance')
proposal = InlineKeyboardButton('✅ Что мы предлагаем', callback_data='proposal')
advantages = InlineKeyboardButton('✅ Преимущества проекта', callback_data='advantages')
commercialization = InlineKeyboardButton('✅ Перспектива коммерциализации результата',
                                         callback_data='commercialization')
intellectual_property = InlineKeyboardButton('✅ Защита прав на интеллектуальную собственность',
                                             callback_data='intellectual_property')
buy_product = InlineKeyboardButton('✅ Купить продукт', callback_data='buy_product')

start_keyboard = InlineKeyboardMarkup(row_width=1).add(about_project, relevance, proposal,
                                                       advantages, commercialization,
                                                       intellectual_property, buy_product)

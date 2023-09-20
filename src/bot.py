from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

import config
from core.states import BuySubscription, BuyUSB

from modules import register_all_handlers
from modules.start import keyboards
from messages import start_messages
from core import keyboards

bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def __on_start_up(dispatcher: Dispatcher) -> None:
    register_all_handlers(dispatcher)


@dp.message_handler(commands=["start"])
async def command_start(message=types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=start_messages.MESSAGE_FOR_COMMAND_START,
                           reply_markup=keyboards.to_start1_keyboard)


async def start_keyboard(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Меню', reply_markup=keyboards.start_keyboard)

    await callback_query.answer()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=BuySubscription.contact)
async def get_user_contact_for_subscription(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваши данные добавлены. Скоро с вами свяжутся.',
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id,
                           text='Вернуться в главное меню',
                           reply_markup=keyboards.to_start_keyboard)

    data = await state.get_data()
    await bot.send_message(chat_id=config.CHAT_ID_FOR_MESSAGES, text=f'Имя: {data.get("name")}\n'
                                                              f'Ссылка: t.me/{message.from_user.username}\n'
                                                              f'Номер телефона: {message.contact.phone_number}\n'
                                                              f'Тариф: Подписка на месяц')

    await state.finish()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=BuyUSB.contact)
async def get_user_contact_for_usb(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваши данные добавлены. Скоро с вами свяжутся.',
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id,
                           text='Вернуться в главное меню',
                           reply_markup=keyboards.to_start_keyboard)

    data = await state.get_data()
    await bot.send_message(chat_id=config.CHAT_ID_FOR_MESSAGES, text=f'Имя: {data.get("name")}\n'
                                                      f'Ссылка: t.me/{message.from_user.username}\n'
                                                      f'Номер телефона: {message.contact.phone_number}\n'
                                                      f'Тариф: Флешка')

    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
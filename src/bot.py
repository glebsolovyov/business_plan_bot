from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

import config

from modules import register_all_handlers
from modules.start import keyboards
from messages import start_messages
from core.keyboards import to_start1_keyboard

bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def __on_start_up(dispatcher: Dispatcher) -> None:
    register_all_handlers(dispatcher)


@dp.message_handler(commands=["start"])
async def command_start(message=types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=start_messages.MESSAGE_FOR_COMMAND_START,
                           reply_markup=to_start1_keyboard)


async def start_keyboard(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Меню', reply_markup=keyboards.start_keyboard)

    await callback_query.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
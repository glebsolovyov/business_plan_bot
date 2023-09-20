from aiogram.dispatcher.filters.state import StatesGroup, State


class BuySubscription(StatesGroup):
    name = State()
    contact = State()


class BuyUSB(StatesGroup):
    name = State()
    contact = State()
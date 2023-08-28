from aiogram import Dispatcher


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from modules.main.handlers import register_main_handlers
    from modules.start.handlers import register_start_handlers

    handlers = [
        register_main_handlers,
        register_start_handlers
    ]

    for handler in handlers:
        handler(dispatcher)

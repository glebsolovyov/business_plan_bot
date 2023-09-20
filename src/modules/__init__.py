from aiogram import Dispatcher


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from modules.main.handlers import register_main_handlers
    from modules.start.handlers import register_start_handlers
    from modules.buy_product.handlers import register_buy_product_handlers

    handlers = [
        register_main_handlers,
        register_start_handlers,
        register_buy_product_handlers
    ]

    for handler in handlers:
        handler(dispatcher)

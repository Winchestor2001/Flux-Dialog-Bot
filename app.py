from aiogram.utils.token import TokenValidationError
from aiogram.types import BotCommand
import asyncio
import logging

from loader import bot, dp
from handlers import router


async def set_commands():
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)


async def main():
    try:
        logging.info("Бот запускается...")
        await set_commands()
        dp.include_router(router)
        await dp.start_polling(bot)
    except TokenValidationError:
        logging.error("Ошибка: Токен бота неверный. Проверьте файл конфигурации!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")
GROUP_ID = env.str("GROUP_ID")
if not TOKEN:
    raise ValueError("Токен не найден! Установите переменную окружения BOT_TOKEN.")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

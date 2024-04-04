from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import config


storage = MemoryStorage()
bot = Bot(token=config.env_values["TOKEN"], parse_mode="HTML")
dp = Dispatcher(storage=storage)

# bot = Bot(token="", parse_mode="html")
# dp = Dispatcher(bot=bot, storage=storage)


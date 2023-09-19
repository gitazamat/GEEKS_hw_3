from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 5152697686
ANIMATION_PIC = '/Users/Lenovo/PycharmProjects/pythonProject2geeks_33-1_Python_month_3/media/joinblink-blink.gif'
GROUP_ID = -1001886494144
DESTINATION_DIR = '/Users/Lenovo/PycharmProjects/pythonProject2geeks_33-1_Python_month_3/media/'
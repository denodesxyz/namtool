from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile
import keyboards
import text
from database import users
from utils import is_admin


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    if not users.user_exists(msg.from_user.id):
        users.add_user(msg.from_user.id)
        lang = "en"
    else:
        lang = users.get_user_settings(msg.from_user.id, "lang")

    username = ""
    if msg.from_user.username:
        username = msg.from_user.username
    else:
        username = msg.from_user.first_name
        
    await msg.answer_photo(caption=text.get_start_msg(lang).format(username=username),
        photo=FSInputFile("start.png"),
        reply_markup=keyboards.get_menu(lang, is_admin(msg.from_user.id)),
        disable_web_page_preview=True)

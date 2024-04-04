from aiogram import Router, F
from aiogram.types import Message, FSInputFile
# from loader import storage, bot
import keyboards
from database import users
from aiogram.fsm.context import FSMContext
import states
import utils
import text


router = Router()

@router.message(F.text.in_({"Mailing"}))
async def process_mailing(msg: Message, state: FSMContext):
    userID = msg.from_user.id
    # only admins can access this command
    if not utils.is_admin(userID):
        return
    lang = users.get_user_settings(userID, "lang")
    await msg.answer("Send message for mailing", reply_markup=keyboards.get_back(lang))
    await state.set_state(states.AdminMailing.message)


@router.message(states.AdminMailing.message)
async def process_mailing_message(msg: Message, state: FSMContext):
    success = 0
    failure = 0
    userID = msg.from_user.id
    lang = users.get_user_settings(userID, "lang")
    m = await msg.answer("Mailing in progress, please, wait...")
    for user in users:
        try:
            await msg.copy_to(user["userID"])
            success += 1
        except Exception as e:
            failure += 1
            continue
    await m.edit_text(f"Mailing done.\nSuccess: {success}\nFailure: {failure}")
    await msg.answer_photo(caption=text.get_start_msg(lang).format(username=msg.from_user.username),
                    photo=FSInputFile("start.png"),
                     reply_markup=keyboards.get_menu(lang, True),
                     disable_web_page_preview=True)
    await state.clear()
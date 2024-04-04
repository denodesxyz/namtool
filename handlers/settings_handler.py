from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards
import text
from database import users, nodes
from aiogram.types import Message, FSInputFile
import states
from utils import is_admin


router = Router()

@router.message(F.text.in_({"Settings", "Настройки", "Налаштування"}))
async def process_test(msg: Message):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_settings_text(lang), reply_markup=keyboards.get_settings(lang))


@router.message(F.text.in_({"Node Alert", "Alert Ноди", "Alert Ноды"}))
async def process_node_alert(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_node_alert(lang), reply_markup=keyboards.get_yes_no(lang), disable_web_page_preview=True)
    await state.update_data({"setting_name": "nodeAlert"})
    await state.set_state(states.Settings.yesno)


@router.message(F.text.in_({"Governance Alert", "Alert Управления", "Alert Управління"}))
async def process_vote_alert(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_vote_alert(lang), reply_markup=keyboards.get_yes_no(lang), disable_web_page_preview=True)
    await state.update_data({"setting_name": "voteAlert"})
    await state.set_state(states.Settings.yesno)


@router.message(F.text.in_({"Network Alert", "Alert Сети", "Alert Мережі"}))
async def process_halt_alert(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_halt_alert(lang), reply_markup=keyboards.get_yes_no(lang), disable_web_page_preview=True)
    await state.update_data({"setting_name": "haltAlert"})
    await state.set_state(states.Settings.yesno)


@router.message(states.Settings.yesno)
async def process_state_nodealert(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    data = await state.get_data()
    users.change_user_settings(msg.from_user.id, data["setting_name"], 1 if msg.text.lower() in ["yes", "да", "так"] else 0)
    await msg.answer(text.get_success_text(lang), reply_markup=keyboards.get_settings(lang))
    await state.clear()


@router.message(F.text.in_({"Remove Node", "Удалить ноду", "Видалити ноду"}))
async def process_remove_node(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_remove_node(lang), reply_markup=keyboards.get_yes_no(lang), disable_web_page_preview=True)
    await state.set_state(states.RemoveNode.yesno)


@router.message(states.RemoveNode.yesno)
async def process_state_removenode(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_success_text(lang), reply_markup=keyboards.get_settings(lang))
    nodes.remove_user_node(msg.from_user.id)
    await state.clear()


@router.message(F.text.in_({"Language", "Язык", "Мова"}))
async def process_language(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_language(lang), reply_markup=keyboards.get_language(lang))
    await state.set_state(states.Language.lang)


@router.message(states.Language.lang)
async def process_state_removenode(msg: Message, state: FSMContext):
    admin = is_admin(msg.from_user.id)
    if msg.text == "English 🇬🇧":
        await msg.answer("Successfully changed language to English", reply_markup=keyboards.get_menu("en", admin))
        users.change_user_settings(msg.from_user.id, "lang", "en")
    elif msg.text == "Ukrainian 🇺🇦":
        await msg.answer("Успішно змінено мову на українську", reply_markup=keyboards.get_menu("ua", admin))
        users.change_user_settings(msg.from_user.id, "lang", "ua")
    elif msg.text == "Russian 🇷🇺":
        await msg.answer("Язык успешно изменен на русский", reply_markup=keyboards.get_menu("ru", admin))
        users.change_user_settings(msg.from_user.id, "lang", "ru")
    else:
        await msg.answer("Please choose language from the list below")
        return
    await state.clear()


@router.message(F.text.in_({"Contact Us", "Свяжитесь с нами", "Зв'яжіться з нами"}))
async def process_contact_us(msg: Message):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_contact_us(lang), disable_web_page_preview=True)


@router.message(F.text.in_({"Back", "Назад"}))
async def process_back(msg: Message, state: FSMContext):
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
    await state.clear()

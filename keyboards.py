from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu(lang, is_admin=False):
    builder = ReplyKeyboardBuilder()
    if lang == "ru":
        builder.row(
            types.KeyboardButton(text="Статус Ноды"),
            types.KeyboardButton(text="Статус Сети")
        )
        builder.row(
            types.KeyboardButton(text="Запуск Ноды"),
            types.KeyboardButton(text="Больше информации о Namada")
        )
        builder.row(
            types.KeyboardButton(text="Настройки")
        )
    elif lang == "ua":
        builder.row(
            types.KeyboardButton(text="Статус Ноди"),
            types.KeyboardButton(text="Статус Мережі")
        )
        builder.row(
            types.KeyboardButton(text="Запуск Ноди"),
            types.KeyboardButton(text="Більше інформації про Namada")
        )
        builder.row(
            types.KeyboardButton(text="Налаштування")
        )
    else:
        builder.row(
            types.KeyboardButton(text="Node Status"),
            types.KeyboardButton(text="Network Status")
        )
        builder.row(
            types.KeyboardButton(text="Run a Node"),
            types.KeyboardButton(text="Explore Namada")
        )
        builder.row(
            types.KeyboardButton(text="Settings")
        )
    if is_admin:
        builder.row(
            types.KeyboardButton(text="Mailing")
        )

    return builder.as_markup(resize_keyboard=True)


# lang param is not used
def get_networks(lang):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Shielded Expedition"),
    )
    builder.row(
        types.KeyboardButton(text="Campfire Testnet"),
    )
    builder.row(
        types.KeyboardButton(text="Namada Mainnet (Upcoming)")
    )
    return builder.as_markup(resize_keyboard=True)


# lang param is not used
def get_language(lang):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="English 🇬🇧"),
    )
    builder.row(
        types.KeyboardButton(text="Ukrainian 🇺🇦"),
    )
    builder.row(
        types.KeyboardButton(text="Russian 🇷🇺")
    )
    return builder.as_markup(resize_keyboard=True)
    

def get_settings(lang):
    builder = ReplyKeyboardBuilder()
    if lang == "ru":
        builder.row(
            types.KeyboardButton(text="Alert Ноды"),
            types.KeyboardButton(text="Alert Управления"),
            types.KeyboardButton(text="Alert Сети"),
        )
        builder.row(
            types.KeyboardButton(text="Удалить ноду"),
            types.KeyboardButton(text="Язык")
        )
        builder.row(
            types.KeyboardButton(text="Свяжитесь с нами")
        )
        builder.row(
            types.KeyboardButton(text="Назад")
        )
    elif lang == "ua":
        builder.row(
            types.KeyboardButton(text="Alert Ноди"),
            types.KeyboardButton(text="Alert Управління"),
            types.KeyboardButton(text="Alert Мережі")
        )
        builder.row(
            types.KeyboardButton(text="Видалити ноду"),
            types.KeyboardButton(text="Мова")
        )
        builder.row(
            types.KeyboardButton(text="Зв'яжіться з нами")
        )
        builder.row(
            types.KeyboardButton(text="Назад")
        )
    else:
        builder.row(
            types.KeyboardButton(text="Node Alert"),
            types.KeyboardButton(text="Governance Alert"),
            types.KeyboardButton(text="Network Alert"),
        )
        builder.row(
            types.KeyboardButton(text="Remove Node"),
            types.KeyboardButton(text="Language")
        )
        builder.row(
            types.KeyboardButton(text="Contact Us")
        )
        builder.row(
            types.KeyboardButton(text="Back")
        )
    return builder.as_markup(resize_keyboard=True)


def get_yes_no(lang):
    builder = ReplyKeyboardBuilder()
    if lang == "ru":
        builder.row(
            types.KeyboardButton(text="Да"),
        )
        builder.row(
            types.KeyboardButton(text="Нет"),
        )
    elif lang == "ua":
        builder.row(
            types.KeyboardButton(text="Так"),
        )
        builder.row(
            types.KeyboardButton(text="Ні"),
        )
    else:
        builder.row(
            types.KeyboardButton(text="Yes"),
        )
        builder.row(
            types.KeyboardButton(text="No"),
        )
    return builder.as_markup(resize_keyboard=True)


def get_back(lang):
    builder = ReplyKeyboardBuilder()
    if lang == "ru":
        builder.row(
            types.KeyboardButton(text="Назад"),
        )
    elif lang == "ua":
        builder.row(
            types.KeyboardButton(text="Назад"),
        )
    else:
        builder.row(
            types.KeyboardButton(text="Back"),
        )
    return builder.as_markup(resize_keyboard=True)

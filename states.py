from aiogram.fsm.state import State, StatesGroup


class Settings(StatesGroup):
    yesno = State()

class RemoveNode(StatesGroup):
    yesno = State()

class Language(StatesGroup):
    lang = State()

class CreateNode(StatesGroup):
    newnode = State()

class NetworkStatus(StatesGroup):
    status = State()

class AdminMailing(StatesGroup):
    message = State()

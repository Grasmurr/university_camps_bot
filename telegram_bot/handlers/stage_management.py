from telebot.handler_backends import State, StatesGroup


class MainMenuStates(StatesGroup):
    initial = State()


class DocumentStates(StatesGroup):
    main = State()
    uni_docs = State()
    children_docs = State()


class OrganisationStates(StatesGroup):
    initial = State()


class States(StatesGroup):
    initial = State()
    documents = State()


class EmergencyStates(StatesGroup):
    initial = State()


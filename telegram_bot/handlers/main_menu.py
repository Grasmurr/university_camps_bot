from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from telebot.handler_backends import State, StatesGroup
import telegram_bot.loader as b
from .stage_management import MainMenuStates

bot = b.bot


def get_id(message):
    return message.from_user.id, message.chat.id


def make_keyboard_markup(*kwargs):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in kwargs:
        markup.add(KeyboardButton(f'{i}'))
    return markup


@bot.message_handler(commands=['start'])
def start_message(message: Message):
    user_id, chat_id = get_id(message)
    bot.set_state(user_id, MainMenuStates.initial, chat_id)
    markup = make_keyboard_markup('Чрезвычайные ситуации', 'Памятка о реализации проекта', 'Памятка об организации проекта',
                                  'Документы', 'Медицинское сопровождение', 'Информация по логистике',
                                  'Сувенирная продукция', 'Связаться с нами')
    my_photo = 'AgACAgIAAxkBAAIGtmSepILqOa2XF59rz_9W11HepW3vAAIbzTEbtCLwSDTW6lYxgcijAQADAgADeQADLwQ'

    bot.send_photo(user_id, photo='AgACAgIAAxkBAAM5ZIrvGXAJn4S9LJ2tA_bcZ2NZPCwAAl_IMRtpAVhIYwaT1GCq8I0BAAMCAAN5AAMvBA',
                   caption='Добро пожаловать в техподдержку от оперативного штаба '
                           'проекта "Университетские смены". \n\n'
                           'Здесь вы можете найти ответы на самые частые вопросы, '
                           'а также найти необходимые документы', reply_markup=markup)
    # bot.send_photo(user_id, photo=my_photo,
    #                caption='Добро пожаловать в техподдержку от оперативного штаба '
    #                        'проекта "Университетские смены". \n\n'
    #                        'Здесь вы можете найти ответы на самые частые вопросы, '
    #                        'а также найти необходимые документы', reply_markup=markup)





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


@bot.message_handler(func=lambda message: message.text == 'Связаться с нами')
def faq(message: Message):
    user_id, chat_id = get_id(message)

    text = '*Для связи с горячей линией оперативного штаба доступны ' \
           'следующие номера телефонов, работающие круглосуточно:*\n\n' \
           'Городской: 8 (800) 101-19-72\n' \
           'Мобильный: 8 (499) 577-02-31\n\n' \
           'Электронная почта: \nДля направления запросов по электронной почте используйте адрес' \
           ' UniverSmena@yandex.ru.'
    bot.send_message(user_id, text, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == 'Информация по логистике')
def logistics(message: Message):
    user_id, chat_id = get_id(message)

    text = '*Информация по логистике и контактным данным оперативного штаба*\n\n' \
           'Общая точка сбора детей – г. Ростов-на-Дону. Вокзал «Ростов-Главный».\n\n' \
           'Ответственный по вопросам организации перевозок: Олег Викторович +7 962 996-63-01'

    bot.send_message(user_id, text, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == 'Сувенирная продукция')
def logistics(message: Message):
    user_id, chat_id = get_id(message)

    text = '*Сувенирная продукция*\n\nПредоставляется полный комплект сувенирной продукции: блокноты, панамы, ручки, ' \
           'свитшоты, шопперы, баннеры, рюкзаки, футболки\\. Все позиции являются обязательными\\.\n\nИспользование ' \
           'логотипа: Логотип Университета разрешено размещать только на баннерах\\.\n\nПолучение материалов: все ' \
           'необходимые материалы для изготовления сувенирной продукции доступны по ссылке: [тут](https://disk\\.ya' \
           'ndex\\.ru/d/KTQPlsUQ\\_keFxA)'

    bot.send_message(user_id, text=text, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda message: message.text == 'Медицинское сопровождение')
def medical_support(message: Message):
    user_id, chat_id = get_id(message)
    text = ('В целях охраны и укрепления здоровья детей и подростков образовательная организация должна быть '
            'укомплектована подготовленным медицинским работником на период проведения образовательной программы.'
            '\n\nОрганизатор поездки должен обеспечить всех участников группы детей полисом медицинского '
            'страхования.\n\nПолис медицинского страхования должен включать:\n-	страхование жизни и '
            'здоровья детей и сопровождающих;\n-	страхование от несчастных случаев;\n-	возможность '
            'госпитализации;\n-	возможность оказания первой помощи;\n-	сумма страхования от 500 тыс. рублей. ')
    bot.send_message(chat_id=user_id, text=text)
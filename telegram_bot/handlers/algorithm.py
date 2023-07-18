from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from telebot import custom_filters
import telegram_bot.loader as b
from .stage_management import DocumentStates, MainMenuStates
from .main_menu import start_message

bot = b.bot


def get_id(message):
    return message.from_user.id, message.chat.id


def make_keyboard_markup(*kwargs):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in kwargs:
        markup.add(KeyboardButton(f'{i}'))
    return markup


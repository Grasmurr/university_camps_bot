from telebot import TeleBot
from .data.config import token
from telebot.storage import StateMemoryStorage


bot = TeleBot(token, state_storage=StateMemoryStorage())


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    bot.send_message(message.from_user.id, f"Received photo with id: {file_id}")
    print(f"Received photo with id: {file_id}")
    bot.send_photo(message.chat.id, file_id)


@bot.message_handler(content_types=['document'])
def handle_document(message):
    file_id = message.document.file_id
    bot.send_message(message.from_user.id, f"Received document with id: {file_id}")
    bot.send_document(message.chat.id, file_id)

from .loader import bot
import telegram_bot.handlers


def run_bot():
    try:
        bot.send_message(305378717, f'Бот запущен!')
        bot.infinity_polling()
    except Exception as e:
        bot.send_message(305378717, f'Ошибка: {e}')

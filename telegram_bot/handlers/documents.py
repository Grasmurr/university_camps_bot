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


@bot.message_handler(func=lambda message: message.text == 'Документы')
def documents_menu(message: Message):
    user_id, chat_id = get_id(message)
    bot.set_state(user_id=user_id, state=DocumentStates.main, chat_id=chat_id)
    markup = make_keyboard_markup('Справки для детей', 'Документы для ВУЗа', 'Согласие на обработку персональных данных',
                                  'Использование шаблонов документов', 'Формирование и предоставление списков детей',
                                  '◀️ назад')

    bot.send_message(user_id, 'Итак, ниже есть категории документов, которые вы можете здесь получить',
                     reply_markup=markup)


@bot.message_handler(state=DocumentStates.main, content_types=['text'])
def back(message: Message):
    response = message.text
    user_id, chat_id = get_id(message)
    if response == '◀️ назад':
        start_message(message)
    elif response == 'Документы для ВУЗа':
        text = ('*Пакет документов, требующийся от вузов*\n\n3.1.1.	Приказ об ответственных: указывает лиц, '
                'отвечающих за реализацию проекта.\n\n3.1.2.	Договор на питание: регулирует условия питания участников '
                'смены (при наличии собственного пункта питания договор не требуется).\n\n3.1.3.	Договор на перевозку: '
                'определяет параметры транспортировки группы.\n\n3.1.4.	Заявка на сопровождение ГИБДД: гарантирует '
                'безопасность транспортировки.\n\n3.1.4 - 1.	ГИБДД – при организованной перевозке групп детей '
                'автобусами'
                '(по ссылке https://гибдд.рф/transportation). \n\n3.1.4 - 2.	Подача уведомления об организованной '
                'перевозке группы детей осуществляется не позднее 48 часов до начала перевозки в междугородном '
                'сообщении'
                'и не позднее 24 часов до начала перевозок в городском и пригородном сообщениях (п. 5 Постановления'
                ' Правительства РФ от 23 сентября 2020 г. N 1527). ссылка\n\n3.1.4 - 3.	В случае если перевозка '
                'осуществляется 3 автобусами и более, перед началом осуществления такой перевозки подается заявка на '
                'сопровождение автобусов патрульным автомобилем (патрульными автомобилями) подразделения '
                'Госавтоинспекции'
                '(п.3 Постановления Правительства РФ от 23 сентября 2020 г. N 1527)\n\nДля упрощения работы с '
                'документацией'
                ' предлагаем использовать готовые шаблоны, доступные по ссылке: https://disk.yandex.ru/d/8RcoLBLwPJXJ-w')
        bot.send_message(user_id, text=text, parse_mode='Markdown')
    elif response == 'Справки для детей':
        bot.send_document(document='BQACAgIAAxkBAAIHeGSewNzDim_nc0ns8qeAahOvHaLoAAJuLQACDSbxSGKRL670xTK1LwQ',
                          chat_id=user_id, caption='Перечень необходимых документов, требующихся для '
                                                   'зачисления детей в образовательно-туристскую программу «'
                                                   'Университетские смены» 2023')

    elif response == 'Согласие на обработку персональных данных':
        text = ('В соответствии с федеральным законом от 27.07.2006 № 152-ФЗ каждый участник программы должен '
                'предоставить согласие на обработку его персональных данных.')
        bot.send_message(user_id, text=text, parse_mode='Markdown')
    elif response == 'Использование шаблонов документов':
        text = ('Приказы, списки детей/сопровождающих, медицинские справки и пр. могут быть подготовлены '
                'с использованием шаблонов, доступных по https://disk.yandex.ru/d/tAuRkWDIZfYSeA')
        bot.send_message(user_id, text=text, parse_mode='Markdown')
    elif response == 'Формирование и предоставление списков детей':
        text = ('Списки детей формируются на основании заявлений на участие в программе «Университетские смены».'
                ' \n\nПримеры заявлений и формат списков можно найти по ссылке https://disk.yandex.ru/d/S1UQakyKuoP8Ig')
        bot.send_message(user_id, text=text, parse_mode='Markdown')


@bot.message_handler(state=DocumentStates.uni_docs, func=lambda message: message.text == '◀️ назад')
def back(message: Message):
    documents_menu(message)


@bot.message_handler(state=DocumentStates.uni_docs)
def get_uni_docs(message: Message):
    user_id, chat_id = get_id(message)
    needed_doc = message.text
    if needed_doc == 'Приказ об ответственных':
        bot.send_message(user_id, text='Приказ об ответственных: указывает лиц, отвечающих за реализацию проекта.'
                                       '\nШаблон доступен по ссылке: \n\n'
                                       'https://docs.google.com/document/d/11PLkPra7Banp07ib9vuAveppKLLI6F7p/'
                                       'edit?usp=share_link&ouid=115567401292289680514&rtpof=true&sd=true')
    elif needed_doc == 'Договор на питание':
        bot.send_message(user_id, text='Договор на питание: регулирует условия питания участников смены'
                                       ' (при наличии собственного пункта питания договор не требуется).'
                                       '\nШаблон доступен по ссылке: \n\n'
                                       'https://docs.google.com/document/d/116hfn1XkCfpOcmHwbVQ0PdRQRpfnt_MF/'
                                       'edit?usp=share_link&ouid=115567401292289680514&rtpof=true&sd=true')
    elif needed_doc == 'Договор на перевозку':
        bot.send_message(user_id, text='Договор на перевозку: определяет параметры транспортировки группы.'
                                       '\nШаблон доступен по ссылке: \n\n'
                                       'https://docs.google.com/document/d/1vUDL4jkowIxj-cIr_kJC72FyJZTFth_d/'
                                       'edit?usp=share_link&ouid=115567401292289680514&rtpof=true&sd=true')
    elif needed_doc == 'Заявка на сопровождение ГИБДД':
        bot.send_message(user_id, text='Заявка на сопровождение ГИБДД: гарантирует безопасность транспортировки.'
                                       '\nШаблон доступен по ссылке: \n\n'
                                       'https://docs.google.com/document/d/12ohdyHXw34gOzyIktD1Kr_v-V5q8QXsZ/'
                                       'edit?usp=share_link&ouid=115567401292289680514&rtpof=true&sd=true')
    elif needed_doc == 'Формирование и предоставление списков детей':
        bot.send_message(user_id, text='Списки детей формируются на основании заявлений на участие в '
                                       'программе «Университетские смены». \n\nШаблон документа можно посмотреть '
                                       'по ссылке: \nhttps://docs.google.com/spreadsheets/d/1C4-0tfsisvUa4jk'
                                       'OSKeMeNl_GwQelgAA/edit?usp=share_link&ouid=115567401292289680514'
                                       '&rtpof=true&sd=true')
    elif needed_doc == 'Медицинское сопровождение':
        bot.send_message(user_id, text='В целях охраны и укрепления здоровья детей и подростков '
                                       'образовательная организация должна быть укомплектована '
                                       'подготовленным медицинским работником на период проведения '
                                       'образовательной программы. \nОрганизатор поездки должен обеспечить '
                                       'всех участников группы детей полисом медицинского страхования.\n\n'
                                       'Полис медицинского страхования должен включать:\n\n'
                                       '- Страхование жизни и здоровья детей и сопровождающих;\n'
                                       '- Страхование от несчастных случаев;\n- Возможность госпитализации; '
                                       '\n- Возможность оказания первой помощи;\n- '
                                       'Сумма страхования от 500 тыс. рублей. ')


@bot.message_handler(state=DocumentStates.children_docs, func=lambda message: message.text == '◀️ назад')
def back(message: Message):
    documents_menu(message)


bot.add_custom_filter(custom_filters.StateFilter(bot))


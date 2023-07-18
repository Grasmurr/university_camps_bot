from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telebot import custom_filters
import telegram_bot.loader as b
from .stage_management import DocumentStates, MainMenuStates
from .main_menu import start_message

bot = b.bot


def get_id(call: CallbackQuery):
    return call.from_user.id, call.message.message_id


def make_next_markup(k):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Далее', callback_data='next_about')
    button2 = InlineKeyboardButton(text='Назад', callback_data='back_about')
    button3 = InlineKeyboardButton(text='Закрыть', callback_data='close_about')
    if k == 0:
        markup.add(button1)
        markup.add(button3)
    elif 0 < k < len(info) - 1:
        markup.add(button2, button1)
        markup.add(button3)
    else:
        markup.add(button2)
        markup.add(button3)
    return markup


user_states = {}

info = ['5.1. Образовательно- туристические программы «Университетские смены» реализуются в соответствии с '
        'поручениями Президента Российской Федерации по итогам заседания Государственного Совета Российской'
        ' Федерации 22 декабря 2022 года от 29.12.2022 г. № Пр-173ГС.\n\n5.2.  '
        'В рамках реализации образовательно- туристические программы «Университетские смены» образовательная '
        'организация высшего образования разрабатывает и утверждает дополнительную общеразвивающую программу '
        'созданую с целью организации непрерывного образовательного и воспитательного процесса. Программа '
        'построена на основах единства и преемственности общего и дополнительного образования, способствует '
        'развитию лидерских качеств, активизации подростков и вовлечению их в созидательную добровольческую, '
        'экологическую, творческую и иную деятельность.\n\n5.3.   Программа предусматривает приобщение '
        'обучающихся к российским традиционным духовно-нравственным ценностям, включая культурные ценности '
        'своей этнической группы, погружение в историю народов России, воспитание чувства сопричастности к '
        'общим корням и ответственности за судьбу народов России и мира в целом, правилам и нормам поведения '
        'в российском обществе.\n\n5.4.   Программа предполагает вариативность и способность к содержательно-'
        'функциональному трансформированию.\n\n5.5.    Ежедневный распорядок дня предусматривает оказание '
        'психолого-педагогической поддержки и сопровождение участников смены, а также традиционную отрядную работу'
        ' с временным подростковым коллективом. ',

        '5.6. Общая программа смены построена с учетом комплексности и непрерывности педагогического воздействия и '
        'включает в себя следующие взаимосвязанные тематические блоки:\n-	тематический блок – профориентационный,'
        ' знакомит с деятельностью образовательной организации высшего образования;\n-	тематический блок – '
        'раскрывает миссию, ценности и направления Движения Первых;\n-	тематический блок – культурно-просветительс'
        'кий.\n\n5.7.   Первый тематический блок может быть представлен следующими мероприятиями: Презентация програ'
        'ммы смены, вуза, Цикл просветительских занятий «Старт в профессию», Профессиональные пробы «Узнавай. Включ'
        'айся. Действуй», Тематические экскурсии «Мир профессий», Цикл творческих встреч «Найди призвание» и т.п.'
        '\n\n5.8.   Второй тематический блок представлен следующими мероприятиями: Тематические огоньки/ разговоры о'
        ' важном, Тематический вечер «Быть с Россией»/ «Я - гражданин своей страны», Социально полезная акция «Доб'
        'рое дело Первых», Тематический день «День Первых», «Классная встреча» с выдающейся личностью региона (спо'
        'ртсмен, деятель культуры и искусства, государственный деятель и др.), Информационно-просветительская акци'
        'я «Первый, Действуй!».\n\n5.9.  Третий тематический блок может быть реализован через проведение мероприят'
        'ий досуга и отдыха.',

        '5.10. Содержание деятельности по планированию отдыха и досуга обучающихся в рамках летнего лагеря '
        '«Университетские'
        ' смены» предполагает реализацию следующих направлений:\n-	оздоровительная деятельность (утренняя зарядка,'
        ' беседы о вредных привычках, спортивные соревнования/часы, подвижные игры, солнечные ванны, и т.п.);\n-	'
        'творческая (коллективно-творческая деятельность, конкурсы, фестивали, викторины, КВН, фотокроссы, мастер-кл'
        'ассы, флэш-мобы и т.п.);\n-	патриотическая (посещение памятных мест, дебаты, музеи, экскурсии, просмотр '
        'кинофильмов, встречи с героями, общественными деятелями, политиками и т.п.);\n-	духовно-нравственная (бесе'
        'ды о нравственности, экскурсии в храм, встречи с духовными лидерами, волонтерские проекты и т.п.);\n-	социаль'
        'но-педагогическая (индивидуальные беседы; групповая работа; анкетирование).\n\n5.11. Приоритетной в организаци'
        'и досуга детей и молодежи следует признать социокультурную деятельность. Культурно-досуговое направление, отра'
        'женное в проектировании массовых досуговых мероприятий (досуговых программ), выступает системообразующим эле'
        'ментом социокультурной деятельности и используется при рекреативно-оздоровительных мероприятиях; включается в'
        ' воспитательные программы организации социально-продуктивной деятельности, формы клубной работы, программы д'
        'етских общественных объединений.',

        '5.12. Классификация досуговых программ по ведущей функции организации культурно-досуговой деятельности:'
        '\n-	историко-патриотические – экскурсии, выставки, акции, экспозиции, посещение памятных и знаковых '
        'мест, знакомство с историей страны, города, края, встречи с героями и политическими лидерам;\n-	просве'
        'тительские - посещение театров, музеев, тематических выставок, творческие встречи, фестивали, мастер-клас'
        'сы и т.п.;\n-	конкурсно-развлекательные, состоящие из разнообразных конкурсов, позволяющих выделить лидир'
        'ующих участников или целые группы в какой-либо области знаний или общественно-полезной деятельности, диск'
        'отеки, стартин и др.;\n-	сюжетно-игровые — в них преобладают разнообразные игры: подвижные, интеллектуа'
        'льные, игры-драматизации, аттракционы, аукционы, флэш-мобы;\n-	фольклорные, включающие народные игры, пес'
        'ни, танцы, хороводы. В сюжет этих программ вводятся персонифицированные образы;\n-	шоу-программы, состоящ'
        'ие из зрелища, пластики, танцев, показа мод, концертных номеров, клоунады, музыки, конкурсы мисс и мистер'
        ', шоу талантов;\n-	рекреационно-оздоровительные, включающие методы биоэнергетического оздоровления, восто'
        'чные оздоровительные системы, шейпинги, аромотерапию, музыкотерапию, арттерапию;\n-	информационно-диск'
        'уссионные, включающие новую и значимую для аудитории информацию, побуждающую к спору, дискуссии, размышле'
        'нию;\n-	праздничные программы, органически сочетающие в себе многообразие содержания и средств художес'
        'твенного воздействия, тематические дни и праздники;\n-	спортивно-развлекательные программы включают подви'
        'жные игры, шуточные поединки, веселые старты, комбинированные эстафеты, спортивные конкурсы, соревнования.'
        ' \n\n5.13. С подробными методическими рекомендациями по разработке образовательной программы ВУЗа можно оз'
        'накомиться по следующей ссылке: https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FQsClojQAqxDtd'
        'nUVhrcO75CLi5jS5sjyTx85%2BTgTZrvpKq%2B8az9Cz56jPWc%2F4Dnlq%2FJ6bpmRyOJonT3VoXnDag%3D%3D%3A%2FМетодрекомен'
        'дации%20к%20программе.docx&name=Методрекомендации%20к%20программе.docx ']


@bot.message_handler(func=lambda message: message.text == 'Памятка о реализации проекта')
def about_project(message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        user_states[user_id] = 0
    curr = user_states[user_id]
    markup = make_next_markup(curr)
    bot.send_message(user_id, text=f'{info[curr]}', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'close_about')
def close_about_message(call: CallbackQuery):
    chat_id, m_id = get_id(call)
    user_states[call.from_user.id] = 0
    bot.edit_message_text(chat_id=chat_id, message_id=m_id, text='Закрыто!')


@bot.callback_query_handler(func=lambda call: call.data in ['next_about', 'back_about'])
def next_message_in_about(call: CallbackQuery):
    chat_id, m_id = get_id(call)
    user_id = call.from_user.id
    if call.data == 'next_about':
        user_states[user_id] += 1
    else:
        user_states[user_id] -= 1
    curr = user_states[user_id]
    markup = make_next_markup(curr)
    bot.edit_message_text(chat_id=chat_id, message_id=m_id, text=f'{info[curr]}', reply_markup=markup)


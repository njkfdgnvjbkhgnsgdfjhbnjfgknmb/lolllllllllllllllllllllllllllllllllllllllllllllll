import telebot
from telebot import types

TOKEN = 'NzIxODg0NzUxNDcxODM3MTg1.XubBkA.wMXsSF_xu38IS5Bnc5K3e48JM_Y'
bot = telebot.TeleBot(TOKEN)
'''
with open('./SH.txt', 'r') as file:
    BOOK = file.read() # открываем книгу и записываем её в BOOK

def pages_keyboard(start, stop):
    """Формируем Inline-кнопки для перехода по страницам.
    """
    keyboard = types.InlineKeyboardMarkup()
    btns = []
    if start > 0: btns.append(types.InlineKeyboardButton(
        text='⬅', callback_data='to_{}'.format(start - 700)))
    if stop < len(BOOK): btns.append(types.InlineKeyboardButton(
        text='➡', callback_data='to_{}'.format(stop)))
    keyboard.add(*btns)
    return keyboard # возвращаем объект клавиатуры

@bot.message_handler(commands=['start'])
def start(m):
    """Отвечаем на команду /start
    """
    bot.send_message(m.chat.id, BOOK[:700], parse_mode='Markdown',
        reply_markup=pages_keyboard(0, 700))
'''
@bot.message_handler(commands=['vibor'])
def vibor(m):
    keyboard = types.InlineKeyboardMarkup()
    #msg = bot.send_message(m.chat.id,'Кто круче???')
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name)
                   for name in ['Витя', 'Теплый', 'Влад']])
    msg = bot.send_message(m.chat.id, 'Кого выбираешь?',
        reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Влад':
        bot.send_message(c.message.chat.id, '*Да, ты прав!*')
    elif c.data == 'Витя':
        bot.send_message(c.message.chat.id, '*Хммммб не полохой выбор Витя!!!*')
    elif c.data == 'Теплый':
        bot.send_message(c.message.chat.id, '*Я так и знал что это ты - Теплый!!!*')
        '''
@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):
    """Редактируем сообщение каждый раз, когда пользователь переходит по
    страницам.
    """
    bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=BOOK[int(c.data[3:]):int(c.data[3:]) + 700],
        parse_mode='Markdown',
        reply_markup=pages_keyboard(int(c.data[3:]),
            int(c.data[3:]) + 700))
'''
bot.polling()
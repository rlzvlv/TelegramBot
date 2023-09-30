import telebot
from telebot import types

bot = telebot.TeleBot('Мой_токен')

# Отслеживаем команду

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Салют, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Обработка текста/ Отправка документов

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет, дорогой", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id} ", parse_mode='html')
    elif message.text == "photo":
        photo = open('Bender_Rodriguez.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать", parse_mode='html')

# Обработка документов

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ага, круто')

# Встроенные в сообщения кнопки

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InLineKeyboardMarkup()
    markup.add(types.InLineKeyboardButton("Посетить сайт", url="https://ru.wikipedia.org/"))
    bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)

# Создание кнопки

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('Википедия')
    start = types.KeyboardButton('Стартуем')
    markup.add(Википедия, Стартуем)
    bot.send_message(message.chat.id, 'Выбери нужное', reply_markup=markup)

# Запускаем на постоянное выполнение

bot.polling(none_stop=True)

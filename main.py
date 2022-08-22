import telebot
from cezar import *
params = {}

bot = telebot.TeleBot('YOUR TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    m = bot.send_message(message.chat.id, f"""\
    Привет, {message.from_user.first_name}, это шифр Цезаря
    """)
    msg = bot.reply_to(m, "Напиши своё послание")
    bot.register_next_step_handler(msg, message_from_user)


def message_from_user(message):
    text = message.text
    params['text'] = text
    msg = bot.reply_to(message, "На какое к-во символов сдвигаем?")
    bot.register_next_step_handler(msg, choose_key)


def choose_key(message):
    key = message.text
    if not key.isdigit():
        msg = bot.reply_to(message, 'Введи цифру')
        bot.register_next_step_handler(msg, choose_key)
        return
    params['key'] = key
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Расшифровка', 'Зашифровать')
    msg = bot.reply_to(message, "Что делаем с посланием?", reply_markup=markup)
    bot.register_next_step_handler(msg, final)


def final(message):
    if message.text == 'Расшифровка':
        bot.send_message(message.chat.id, f"{decoding(params['text'], int(params['key']))}")
    else:
        bot.send_message(message.chat.id, f"{encrypt(params['text'], int(params['key']))}")
    bot.send_message(message.chat.id, text='Для повтора нажми -> /start', )


bot.polling(none_stop=True)

import requests
import telebot

bot = telebot.TeleBot('963712153:AAFHy_zyV91X8Rks7t4LQKRxPP2QmyDTyg4')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard1.row('Прошел', 'Слушок', 'Что ты')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Hi nigga')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Bye nigga')
    elif message.text.lower() == 'Кто я':
        bot.send_sticker(message.chat.id, 'CAADAwADjgIAAsbNxQEarlhixib2CBYE')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
import telebot
from telebot import types
from aiogram.types.web_app_info import WebAppInfo


bot = telebot.TeleBot('6991684025:AAGOByZdl4d29Axt37VStKyQARVugk9sxBQ')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.InlineKeyboardButton(text='Посетить сайт', web_app=types.WebAppInfo(url='https://beshtaxi.uz')))
    bot.send_message(message.chat.id, text='Добро пожаловать на телеграм бот Besh Taxi, бот еще находиться на стадийй разработки, пака же то вы пожите посетить наш сайт нажав на кнопочку ниже.', reply_markup=markup)


bot.polling(non_stop=True)
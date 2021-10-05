import csv
import json
import logging
import os
import re
from datetime import datetime
from urllib.parse import quote

import telebot
from telebot import types

# logger settings

bot = telebot.TeleBot("2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk")


def about(message):
    bot.send_message(message.chat.id,
                     "Бот создан для быстрой помощи школьникам и студентам"
                     " в нахождении материалов по различним темам.\n"
                     "Автор: @erlihigh \n")


def programming(message):
    bot.send_message(message.chat.id, 'Кнопка "Программирование" - работает')


def math_(message):
    bot.send_message(message.chat.id, 'Кнопка "Математика" - работает')


@bot.message_handler(commands=['start'])
def welcome(message):
    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📚 Ищем литературу!")
    item2 = types.KeyboardButton("🎦 Ищем видео!")
    item3 = types.KeyboardButton("Об авторе")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, "
                     "{0.first_name}!\n"
                     "Я - <b>{1.first_name}</b>, "
                     "бот созданный чтобы ты научился чему-то новому."
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def markups(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Программирование")
    item2 = types.KeyboardButton("Математика")
    item3 = types.KeyboardButton("Об авторе")
    markup.add(item1, item2, item3)
    if message.chat.type == 'private':
        if message.text == '📚 Ищем литературу!':
            bot.send_message(message.chat.id, "Что ищем?")
            bot.send_message(message.chat.id, "Отладка, функция пока не работает")
        elif message.text == '🎦 Ищем видео!':
            bot.send_message(message.chat.id, text="На какую тему нужно видео?\n"
                                                   "Есть несколько популярных видео по следующим тематикам"
                                                   "⤵", parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, 'Если нет заданой темы - напиши ее?')
            bot.send_message(message.chat.id, "Отладка, функция пока не работает")
        elif message.text == 'Программирование':
            programming(message)
        elif message.text == 'Математика':
            math_(message)
        elif message.text == 'Об авторе':
            about(message)


bot.polling(none_stop=True)

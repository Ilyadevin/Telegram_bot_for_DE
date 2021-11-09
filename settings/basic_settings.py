import csv
import json
import logging
import os
import re
from datetime import datetime
from urllib.parse import quote
import telebot
from telebot import types
import time

def keyboard_reply():
    markup = types.ReplyKeyboardMarkup( resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("🎦 Ищем видео!")
    item2 = types.KeyboardButton("Об авторе")
    item3 = types.KeyboardButton("/help")
    markup.add(item1, item2, item3)
    return markup


def keyboard_inline():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Математика базовый уровень", callback_data='mathv_b')
    item2 = types.InlineKeyboardButton("Математика профильная", callback_data='mathv_p')
    item3 = types.InlineKeyboardButton("Информатика", callback_data='inf')
    item4 = types.InlineKeyboardButton("Физика", callback_data='ph')
    #item5 = types.InlineKeyboardButton("В предыдущее меню", callback_data='main_menu')
    markup.add(item1, item2, item3, item4)
    return markup


def token_get():
    with open("config.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["telegram_api"]


list_of_links = \
    {"mbase":
        [
            "https://www.youtube.com/watch?v=st_wW14IqQE&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=1",
        ],
        "mprofile":
            [
                "https://www.youtube.com/watch?v=NABPt62mcPs&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=1",
            ],
        "inf":
            [
                "https://www.youtube.com/watch?v=IGMpt2e1yGs"
            ],
        "ph":
            [
                "https://www.youtube.com/watch?v=CtNzHo-EvSQ"
            ]

    }

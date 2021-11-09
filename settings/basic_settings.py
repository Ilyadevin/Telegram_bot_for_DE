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


def token_get():
    with open("config.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["telegram_api"]


list_of_links = \
    {"base":
        [
            "https://www.youtube.com/watch?v=st_wW14IqQE&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=1",
            "https://www.youtube.com/watch?v=X4VzjabpqbU&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=2",
        ],
        "profile_1":
            [
                "https://www.youtube.com/watch?v=NABPt62mcPs&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=1",
                "https://www.youtube.com/watch?v=ePjuT9DKKMo&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=2",
            ]
    }

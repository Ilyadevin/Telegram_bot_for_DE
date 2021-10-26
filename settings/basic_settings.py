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
            "https://www.youtube.com/watch?v=st_wW14IqQE&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=1&t=1s",
            "https://www.youtube.com/watch?v=X4VzjabpqbU&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=2",
            "https://www.youtube.com/watch?v=ZG69CHyD8bk&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=3",
            "https://www.youtube.com/watch?v=wRndThA8Xjo&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=4",
            "https://www.youtube.com/watch?v=lOGVtkhlpw8&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=5",
            "https://www.youtube.com/watch?v=ePjuT9DKKMo&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=6"
        ],
        "profile_1":
            [
                "https://www.youtube.com/watch?v=NABPt62mcPs&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=1&t=6s",
                "https://www.youtube.com/watch?v=ePjuT9DKKMo&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=2&t=2s",
                "https://www.youtube.com/watch?v=SIHaqShre6M&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=3&t=5s",
                "https://www.youtube.com/watch?v=GgCYahQ7yKg&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=4",
                "https://www.youtube.com/watch?v=7IPKIBGk1qo&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=5",
                "https://www.youtube.com/watch?v=ZKGTVfaiGe8&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=6",
                "https://www.youtube.com/watch?v=YrwgTu4X3RY&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=7",
                "https://www.youtube.com/watch?v=0aXmrT2tH04&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=8",
                "https://www.youtube.com/watch?v=WRfItaXfFSY&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=9",
                "https://www.youtube.com/watch?v=f0vxcmdCRoc&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=10",
                "https://www.youtube.com/watch?v=BuRZOyUUN3o&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=11",
                "https://www.youtube.com/watch?v=Z2fMf_qNzhs&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=12",
                "https://www.youtube.com/watch?v=sepMfKeYRQw&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=13",
                "https://www.youtube.com/watch?v=ZjCrG8R5lbw&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=14",
                "https://www.youtube.com/watch?v=ZG69CHyD8bk&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=15",
                "https://www.youtube.com/watch?v=wRndThA8Xjo&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=16",
                "https://www.youtube.com/watch?v=lOGVtkhlpw8&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=17",
                "https://www.youtube.com/watch?v=yLAubeyG0Ac&list=PLzJLbwhmP96PtqZR8BunCNLqFQb6T8bQF&index=18"
            ],
        "profile_2":
            [
                "https://www.youtube.com/watch?v=3xPDOfDzYFk&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=1",
                "https://www.youtube.com/watch?v=cagKYLkc7Ko&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=2",
                "https://www.youtube.com/watch?v=2kP41Sg8L1A&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=3",
                "https://www.youtube.com/watch?v=ZBCpqzWnSd0&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=4",
                "https://www.youtube.com/watch?v=F40ESBPXiNs&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=5",
                "https://www.youtube.com/watch?v=XOz6RcW7Qso&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=6",
                "https://www.youtube.com/watch?v=4sPnvNP6f5o&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=7",
                "https://www.youtube.com/watch?v=oeA5vvHtcpE&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=8",
                "https://www.youtube.com/watch?v=Ynaxu1zHkYM&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=9",
                "https://www.youtube.com/watch?v=wd7S48RJYZ8&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=10",
                "https://www.youtube.com/watch?v=k1jgPMuv6J4&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=11",
                "https://www.youtube.com/watch?v=d9uLqST_KfY&list=PLzJLbwhmP96NaRin41V43SuUCxPo_n3Ni&index=12"
            ]
    }

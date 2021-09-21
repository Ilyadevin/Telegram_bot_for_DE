import json
import telebot
import time
import os

statusd = 'close'
statusw = 'close'
mode = 0
lang = 'ru'


class TokensSettings:
    def __init__(self):
        with open('config.json', 'r', encoding='utf8') as json_file:
            self.reader = json.load(json_file)

    def telegram_main_token(self):
        for token in self.reader:
            telegram_token = token['telegram_api']
            return telegram_token

    def yandex_token(self):
        for token in self.reader:
            yandex_token = token['yandex_api']
            return yandex_token

    def google_settings(self):  # This is the test format
        for settings in self.reader:
            service_urls = [settings['google_settings'][0],settings['google_settings'][1]]
            return service_urls

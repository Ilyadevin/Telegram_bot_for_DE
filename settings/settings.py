import telebot
import random
from telebot import types
import argparse
import googleapiclient
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

bot = telebot.TeleBot("2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk")
youtube_token = "AIzaSyB8UcRYxwa7ITRPQ3kEYYIJYbVCSblH6T0"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def about(message):
    bot.send_message(message.chat.id,
                     "Бот создан для быстрой помощи школьникам и студентам"
                     " в нахождении материалов по различним темам.\n"
                     "Автор: @erlihigh \n"
                     "")


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
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Программирование", callback_data='Программирование')
    item2 = types.InlineKeyboardButton("Математика", callback_data='Математика')
    item3 = types.KeyboardButton("Об авторе")
    markup.add(item1, item2, item3)
    if message.chat.type == 'private':
        if message.text == '📚 Ищем литературу!':
            bot.send_message(message.chat.id, "Что ищем?")
            bot.send_message(message.chat.id, "Отладка, функция пока не работает")
        elif message.text == '🎦 Ищем видео!':
            bot.send_message(message.chat.id, "На какую тему нужно видео?\n"
                                              "Есть несколько популярных видео по следующим тематикам"
                                              "⤵")
            bot.send_message(message.chat.id, 'Если нет заданой темы - напиши ее?')
            bot.send_message(message.chat.id, "Отладка, функция пока не работает")
        elif message.text == 'Об авторе':
            about(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Программирование':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'Математика':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=youtube_token)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part='id,snippet',
        maxResults=options.max_results
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s (%s)' % (search_result['snippet']['title'],
                                       search_result['id']['videoId']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s (%s)' % (search_result['snippet']['title'],
                                         search_result['id']['channelId']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                          search_result['id']['playlistId']))

    print('Videos:\n', '\n'.join(videos), '\n')
    print('Channels:\n', '\n'.join(channels), '\n')
    print('Playlists:\n', '\n'.join(playlists), '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='Google')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
# RUN
bot.polling(none_stop=True)

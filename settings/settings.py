import settings.basic_settings
from settings.basic_settings import *

bot = telebot.TeleBot("2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk")


@bot.message_handler(commands=['start'])
def welcome(message):
    time.sleep(1)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, "
                     "{0.first_name}!\n"
                     "Я - <b>{1.first_name}</b>, \n"
                     "Вместе с сервисом ЕГЭ с ЮКлэва (YouClever) мы поможем вам сдать ЕГЭ на 100!"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=settings.basic_settings.keyboard_reply())


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎦 Ищем видео!':

            time.sleep(1)
            bot.send_message(message.chat.id, "На какую тему нужно видео?\n" "⤵",
                             parse_mode='html', reply_markup=settings.basic_settings.keyboard_inline())
        elif message.text == 'Об авторе':
            bot.send_message(
                message.chat.id,
                'Бот создан на базе библиотеки "telebot"\n'
                '\n'
                'При возникновении ошибок логи автоматически отправляются контактному лицу\n'
                'С предложениями и отзывами можно обратится к автору'
            )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            if call.data == 'mathv_b':
                bot.send_message(call.message.chat.id, 'Далее будут выведены видео с разбором '
                                                       'варианта ЕГЭ по базовой математике')
                time.sleep(1)
                for video_base in range(0, len(list_of_links["mbase"])):
                    video = list_of_links["mbase"][video_base]
                    time.sleep(1.5)
                    bot.send_message(call.message.chat.id, video)
            elif call.data == 'mathv_p':
                for video_profil in range(len(list_of_links["mprofile"])):
                    video = list_of_links["profile_1"][video_profil]
                    time.sleep(1.5)
                    bot.send_message(call.message.chat.id, video)
            elif call.data == 'inf':
                for video_inf in range(len(list_of_links["inf"])):
                    video = list_of_links["profile_1"][video_inf]
                    time.sleep(1.5)
                    bot.send_message(call.message.chat.id, video)
            elif call.data == 'ph':
                for video_ph in range(len(list_of_links["ph"])):
                    video = list_of_links["profile_1"][video_ph]
                    time.sleep(1.5)
                    bot.send_message(call.message.chat.id, video)
    except Exception as e:
        bot.send_message(445431715, f"Возникла ошибка у пользователя - {call.message.message_id} \n"
                                    f"код ошибки {str(e)}")

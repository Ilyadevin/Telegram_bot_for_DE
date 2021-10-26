from settings.basic_settings import *

bot = telebot.TeleBot("2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk")


# Обработка выхода из меню


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item2 = types.KeyboardButton("🎦 Ищем видео!")
    item3 = types.KeyboardButton("Об авторе")

    markup.add(item2, item3)
    time.sleep(1)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, "
                     "{0.first_name}!\n"
                     "Я - <b>{1.first_name}</b>, \n"
                     "Вместе с сервисом ЕГЭ с ЮКлэва (YouClever) мы поможем вам сдать ЕГЭ на 100!"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎦 Ищем видео!':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Математика БАЗА", callback_data='mathv_b')
            item2 = types.InlineKeyboardButton("Математика Профиль", callback_data='mathv_p')

            markup.add(item1, item2)
            time.sleep(1)
            bot.send_message(message.chat.id, "На какую тему нужно видео?\n" "⤵",
                             parse_mode='html', reply_markup=markup)
        elif message.text == 'Об авторе':
            bot.send_message(
                message.chat.id,
                'Бот создан на базе библиотеки "telebot"\n'
                '\n'
                'При возникновении ошибок логи автоматически отправляются контактному лицу\n'
                'С предложениями и отзывами можно обратится к автору - @erlihigh'
            )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # Удаление клавиатуры
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='yes')
            item2 = types.InlineKeyboardButton("Нет", callback_data='no')

            markup.add(item1, item2)
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Отладка завершена", reply_markup=None
            )

            if call.data == 'mathv_b':
                bot.send_message(call.message.chat.id, 'Далее будут выведены видео с разбором '
                                                       'варианта ЕГЭ по базовой математике')
                time.sleep(1)
                for i in range(1, len(list_of_links["base"])):
                    video = list_of_links["base"][i]
                    time.sleep(1)
                    bot.send_message(call.message.chat.id, video)
                    bot.send_message(
                        call.message.chat.id, "Вывести следующее видео?\n" "⤵",
                        reply_markup=markup,
                        parse_mode='html'

                    )
                    # a = 0
                    # if a == 0:
                    #     @bot.callback_query_handler(func=lambda call_: True)
                    #     def call_back_end_of_array(call_):
                    #         if call_.data:
                    #             if call_.data == 'yes':
                    #                 a = 1
                    #                 return True
                    #             elif call_.data == 'no':
                    #                 a = 0
                    #                 return False
                    # elif a == 1:
                    #     a = 0
                    #     continue

                    # if call_back_end_of_array(call) is True:
                    #   print("дошло сюда")
                    #  break
                    # else:
                    #   markup = types.InlineKeyboardMarkup(row_width=2)
                    #  item1 = types.InlineKeyboardButton("Математика БАЗА", callback_data='mathv_b')
                    # item2 = types.InlineKeyboardButton("Математика Профиль", callback_data='mathv_p')
                    # markup.add(item1, item2)
                    # bot.send_message(
                    #    call.message.chat.id, "Выход в предыдущее меню:",
                    #   parse_mode='html', reply_markup=markup
                    # )
                    # break
                # time.sleep(1)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                     text="Отладка завершена", reply_markup=None)
            elif call.data == 'mathv_p':
                # bot.send_message(call.message.chat.id, 'Нужен разбор первой или второй части?')
                time.sleep(1)
                bot.send_message(call.message.chat.id, 'Разбор 1 части профильного варианта математики')
                for i in range(len(list_of_links["profile_1"])):
                    video = list_of_links["profile_1"][i]
                    time.sleep(5)
                    bot.send_message(call.message.chat.id, video)
                time.sleep(1)
                bot.send_message(call.message.chat.id, 'Разбор 2 части профильного варианта математики')
                for i in range(len(list_of_links["profile_2"])):
                    video = list_of_links["profile_2"][i]
                    time.sleep(5)
                    bot.send_message(call.message.chat.id, video)
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Отладка завершена", reply_markup=None
            )

    except Exception as e:
        bot.send_message(445431715, f"Возникла ошибка у пользователя - {call.message.message_id} \n"
                                    f"код ошибки {str(e)}")

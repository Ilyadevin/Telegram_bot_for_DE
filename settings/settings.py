from basic_settings import *

bot = telebot.TeleBot('2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk')


def math_b():
   
    return 'https://www.youtube.com/watch?v=st_wW14IqQE&list=PLzJLbwhmP96PjAAG0fSU5Z9Bf2949Frar&index=1'


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📚 Ищем литературу!")
    item2 = types.KeyboardButton("🎦 Ищем видео!")
    item3 = types.KeyboardButton("Об авторе")

    markup.add(item1, item2, item3)
    time.sleep(1)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, "
                     "{0.first_name}!\n"
                     "Я - <b>{1.first_name}</b>, \n"
                     "Вместе с ЕГЭ с ЮКлэва (YouClever) мы поможем вам сдать ЕГЭ на 100!"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '📚 Ищем литературу!':
            bot.send_message(message.chat.id, text="Отладка, функция пока не работает", parse_mode='html')

        elif message.text == '🎦 Ищем видео!':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Математика БАЗА", callback_data='mathv_b')
            item2 = types.InlineKeyboardButton("Математика Профиль", callback_data='mathv_p')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, "На какую тему нужно видео?\n" "⤵",
                             parse_mode='html', reply_markup=markup)
            time.sleep(1)
            # bot.send_message(message.chat.id, 'Если нет заданой темы - напиши ее, а я попробую разобраться')
            # bot.send_message(message.chat.id, text="Отладка, функция пока не работает", parse_mode='html',
            # reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'mathv_b':
                bot.send_message(call.message.chat.id, 'Кнопка "Математика БАЗА" работает')
                time.sleep(1)
                bot.send_message(call.message.chat.id, math_b())
                time.sleep(1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Отладка завершена", reply_markup=None)
            elif call.data == 'mathv_p':
                bot.send_message(call.message.chat.id, 'Кнопка "Математика Профиль" работает')
            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                     text="Отладка завершена", reply_markup=None)
            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #                          text="Клавиатура закрыта")
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

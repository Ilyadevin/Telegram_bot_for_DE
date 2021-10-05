from basic_settings import *

bot = telebot.TeleBot('2029007087:AAHQVbeZofoMALxBCsa_bmwAS0uU6rEchvk')


@bot.message_handler(commands=['start'])
def welcome(message):
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
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '📚 Ищем литературу!':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Математика", callback_data='mathlit')
            item2 = types.InlineKeyboardButton("Информатика", callback_data='informlit')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, "На какую тему нужна литература?\n"
                                              "⤵")
            bot.send_message(message.chat.id, 'Если нет заданой темы - напиши ее, а я попробую разобраться')
            bot.send_message(message.chat.id, text="Отладка, функция пока не работает", parse_mode='html',
                             reply_markup=markup)
        elif message.text == '🎦 Ищем видео!':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Математика", callback_data='math')
            item2 = types.InlineKeyboardButton("Информатика", callback_data='inform')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, "На какую тему нужно видео?\n"
                                              "Есть несколько популярных видео по следующим тематикам"
                                              "⤵")
            bot.send_message(message.chat.id, 'Если нет заданой темы - напиши ее?')
            bot.send_message(message.chat.id, text="Отладка, функция пока не работает", parse_mode='html',
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'math':
                bot.send_message(call.message.chat.id, 'Кнопка "Математика" работает')
            elif call.data == 'inform':
                bot.send_message(call.message.chat.id, 'Кнопка "Информатика" работает')
            elif call.data == 'mathlit':
                bot.send_message(call.message.chat.id, 'Кнопка литературы по "Математике" работает')
            elif call.data == 'informlit':
                bot.send_message(call.message.chat.id, 'Кнопка литература по "Информатике" работает')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Отладка завершена", reply_markup=None)
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Клавиатура закрыта")
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

from basic_settings import *


def get_keyboard_fab():
    buttons = [
        types.InlineKeyboardButton(text="Математика", callback_data=callback_numbers),
        types.InlineKeyboardButton(text="Информатика", callback_data=callback_numbers),
        types.InlineKeyboardButton(text="Инностранный", callback_data=callback_numbers)
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


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
        elif message.text == 'Об авторе':
            about(message)


@bot.message_handler(commands=['math_'])
def keyboard(message):
    bot.send_message(message.chat.id, 'Кнопка "Математика" - работает')


# fabnum - префикс, action - название аргумента, которым будем передавать значение
callback_numbers = CallbackData("fabnum", "action")


async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard_fab())


@dp.message_handler(commands="numbers_fab")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_numbers.filter(action=["incr", "decr"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data["action"]
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value - 1
        await update_num_text_fab(call.message, user_value - 1)
    await call.answer()


@dp.callback_query_handler(callback_numbers.filter(action=["finish"]))
async def callbacks_num_finish_fab(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f"Итого: {user_value}")
    await call.answer()


bot.polling(none_stop=True)

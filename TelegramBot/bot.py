import config
import telebot
import response_strings

bot = telebot.TeleBot(config.token)
flag_blubbery = None


def get_flag_blubbery():
    return flag_blubbery


def set_flag_blubbery(flag):
    flag_blubbery = flag


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.send_message(message.chat.id, response_strings.help_str + response_strings.weekly_event)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):

    if message.text.lower() == ('осмотреться'):
        response = response_strings.room_1_look_around

    elif message.text.lower() == ('пристально осмотреться') or message.text.lower() == ('пристально осмотреть комнату'):
        response = response_strings.room_1_eat_look_around

    elif message.text.lower().__contains__('голубику'):
        response = response_strings.room_1_eat

    elif message.text.lower().__contains__('карман') or message.text.lower().__contains__('посмотреть в карманы'):
        response = response_strings.room_1_look_in_pockets

    elif message.text.lower().__contains__('осмотреть шкатулку'):
        response = response_strings.box_investigate

    elif message.text.lower() == ('шкатулка 1234'):
        response = response_strings.box_open_success

    elif message.text.lower().__contains__('шкатулк') or message.text == 'шкатулка':
        response = response_strings.box_investigate + response_strings.box_help

    elif message.text.lower().__contains__('прочит'):
        response = response_strings.finish

    else:
        response = response_strings.error

    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    bot.polling(none_stop=True)

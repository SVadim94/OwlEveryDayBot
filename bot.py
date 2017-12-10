from handlers import handlers
import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def calculator(message):
    try:
        cmd = message.text.split(' ')
        handlers.get(cmd[0], handlers['/usage'])(bot, message.chat.id)
    except Exception as e:
        bot.send_message(message.chat.id, 'Exception: %s' % e)

if __name__ == '__main__':
    bot.polling(none_stop=True)

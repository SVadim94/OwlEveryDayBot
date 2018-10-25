import logging
from urllib.request import urlopen

from telegram.ext import CommandHandler, Updater

import config
from owl import get_owl_url


class Bot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.logger = logging.getLogger(__name__)
        
        self.dispatcher.add_handler(CommandHandler("get", self._cmd_get))
        self.dispatcher.add_handler(CommandHandler("about", self._cmd_about))
        self.dispatcher.add_handler(CommandHandler("help", self._cmd_help))

        self.dispatcher.add_error_handler(self.error)

    def error(self, bot, update, error):
        self.logger.error(error)

    def _cmd_get(self, bot, update):
        owl = get_owl_url()

        with urlopen(owl) as f:
            bot.send_photo(
                chat_id=update.message.chat_id,
                photo=f,
                caption="Get your random owl! ;)"
            )
    
    def _cmd_about(self, bot, update):
        update.message.reply_text(
            """The bot is designed to send a random owl to my favourite one :3 Yep, Xenia, I'm talking to you ;)"""
        )

    def _cmd_help(self, bot, update):
        update.message.reply_text("\n"
            "Usage:\n"
            "\n"
            "/get - get a random owl\n"
            "/about - about this bot\n"
            "/help - show this message\n"
        )

    def run(self):
        self.updater.start_polling()


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot = Bot(config.token)
    bot.run()

if __name__ == '__main__':
    main()

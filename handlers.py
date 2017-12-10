from owl import get_owl_url
from urllib.request import urlopen


def usage(bot, chat_id):
    bot.send_message(chat_id, """\
Usage:

/get - get a random owl
/about - about this bot
/usage - show this message
""")


def get_an_owl(bot, chat_id):
    owl = get_owl_url()
    owl = urlopen(owl)
    
    bot.send_photo(chat_id, owl.read(), "Get your random owl! ;)")


def print_about(bot, chat_id):
    bot.send_message(chat_id, """The bot is designed to send a random owl to my favourite one :3""")

handlers = {
    "/get": get_an_owl,
    "/about": print_about,
    "/usage": usage
}

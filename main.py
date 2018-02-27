import os
from telegram.ext import Updater, Filters, MessageHandler

token = "420951309:AAHvzWWNvBD5MwgbB4JO5xWKt1B4oDzToYM"
updater = Updater(token)
PORT = int(os.environ.get('PORT', '5000'))



disp=updater.dispatcher


def ade_tonno(bot, update):
    print(update)
    update.message.repy_text("Ade tonno")


disp.add_handler(MessageHandler(Filters.text,ade_tonno))




updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path="main.py")
updater.bot.set_webhook("https://github.com/nicofirst1/AdeBot/blob/master/main.py")

updater.idle()
print("Starting...")
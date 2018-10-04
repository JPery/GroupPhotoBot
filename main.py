from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

last_uploaded_photo = ""


def echo(bot, update):
    global last_uploaded_photo
    try:
        chat_id = update.message.chat_id
        bot_chat = bot.getChat(chat_id=chat_id)
        if bot_chat['photo']['small_file_id'] != last_uploaded_photo:
            bot.setChatPhoto(chat_id=chat_id, photo=open("telegram.jpg", "rb"))
            last_uploaded_photo = bot.getChat(chat_id=chat_id)['photo']['small_file_id']
    except Exception as e:
        print(e)


TOKEN = ""
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.all, echo))
dispatcher.add_handler(CommandHandler("start", echo))
updater.start_polling(clean=True)

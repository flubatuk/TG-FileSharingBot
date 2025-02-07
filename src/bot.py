from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from handlers.admin import AdminHandler
from handlers.user import UserHandler
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)

    # Initialize handlers
    admin_handler = AdminHandler(updater)
    user_handler = UserHandler(updater)

    # Set up command handlers
    updater.dispatcher.add_handler(CommandHandler('start', user_handler.start))
    updater.dispatcher.add_handler(CommandHandler('upload', admin_handler.upload_file))
    updater.dispatcher.add_handler(CommandHandler('add_admin', admin_handler.add_admin))
    updater.dispatcher.add_handler(CommandHandler('remove_admin', admin_handler.remove_admin))
    updater.dispatcher.add_handler(CommandHandler('check_membership', user_handler.check_membership))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
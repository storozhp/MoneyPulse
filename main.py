from MoneyPulse import bot
from telegram import Update


if __name__ == "__main__":
    bot.run_polling(allowed_updates=Update.ALL_TYPES)

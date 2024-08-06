from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from MoneyPulse.utils import get_user, register_user


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    if get_user(user_id=user.id) is None:
        keyboard = [
            [InlineKeyboardButton("UAH", callback_data="UAH")],
            [InlineKeyboardButton("USD", callback_data="USD")],
            [InlineKeyboardButton("EUR", callback_data="EUR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Main currency", reply_markup=reply_markup)
    else:
        keyboard = [["Курс на сьогодні", "Налаштування"]]
        await update.message.reply_text("Hello", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))


async def reg_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = update.effective_user
    await query.answer()

    register_user(user.username, user.id, query.data)


def register_handlers(bot: Application):
    bot.add_handler(CommandHandler("start", start_cmd))

    bot.add_handler(CallbackQueryHandler(reg_handler))

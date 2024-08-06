from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from MoneyPulse.utils import get_user, register_user


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    if get_user(user_id=user.id) is None:
        keyboard = [
            [InlineKeyboardButton("UAH", callback_data="START_UAH")],
            [InlineKeyboardButton("USD", callback_data="START_USD")],
            [InlineKeyboardButton("EUR", callback_data="START_EUR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        msg = update.message.reply_text("Hello!\n\nI am the MoneyPulse telegram bot, your virtual assistant in the "
                                        "world of currencies. My goal is to tell you the current exchange "
                                        "rates.\n\nLet's first choose the main currency into which I will transfer "
                                        "everything:", reply_markup=reply_markup)
        await msg

        context.user_data["last_message"] = update.message.message_id
    else:
        keyboard = [
            [InlineKeyboardButton("Exchange rates for today", callback_data="MAIN_MENU_today_rates")],
            [InlineKeyboardButton("Settings", callback_data="MAIN_MENU_settings")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(context.user_data["last_message"])
        # BUG: edit last message from bot
        await update.message.edit_text("test", message_id=context.user_data["last_message"], reply_markup=reply_markup)
        # await .message.edit_text("Hello, what are we going to do today?", reply_markup=reply_markup)


async def keyboard_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = update.effective_user
    await query.answer()

    if query.data.find("START") == 0:
        currency = query.data.replace("START_", "")
        register_user(user.username, user.id, currency)
    elif query.data.find("MAIN_MENU") == 0:
        choice = query.data.replace("MAIN_MENU_", "")

        if choice == "today_rates":
            pass
        elif choice == "settings":
            pass


def register_handlers(bot: Application):
    bot.add_handler(CommandHandler("start", start_cmd))

    bot.add_handler(CallbackQueryHandler(keyboard_handler))

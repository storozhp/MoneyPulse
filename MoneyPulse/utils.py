from os import getenv

from dotenv import load_dotenv
from MoneyPulse.database import users_collection

load_dotenv()


def get_bot_token():
    return getenv("TOKEN")


def register_user(username, user_id, main_currency: str):
    users_collection.insert_one({
        "username": username,
        "user_id": user_id,
        "main_currency": main_currency,
        "currency_list": {
            "UAH": False,
            "USD": False,
            "EUR": False
        }
    })


def get_user(user_id):
    user = users_collection.find_one({"user_id": user_id})
    return user

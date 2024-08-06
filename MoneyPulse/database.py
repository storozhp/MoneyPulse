from pymongo.mongo_client import MongoClient

from os import getenv
from dotenv import load_dotenv


load_dotenv()

try:
    client = MongoClient(getenv("MONGO_CLUSTER"))

    database = client["MoneyPulse"]
    users_collection = database["users"]
except Exception as e:
    print(e)

import logging

from telegram.ext import Application
from MoneyPulse.handlers import register_handlers
from MoneyPulse.utils import get_bot_token


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

bot = Application.builder().token(get_bot_token()).build()

register_handlers(bot)

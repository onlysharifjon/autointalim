# from cgitb import text
import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiohttp import request
# from sqlalchemy import true
# from telegram import Contact
startbut = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "HA ✅"),
        ],
        [
            KeyboardButton(text = "YOQ ❌"),
        ],

    ],
    resize_keyboard = True,
)
xodimlar =ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Orqaga🔙"),
        ],
    ],
    resize_keyboard = True,
)
startbutl = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "HA📄"),
        ],
        [
            KeyboardButton(text = "YOQ✖️"),
        ],

    ],
    resize_keyboard = True,
)
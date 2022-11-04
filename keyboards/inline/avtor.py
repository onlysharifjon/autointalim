from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
x = datetime.datetime.now()
admin = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Toshkent shahar", callback_data="toshkentshah"),

        ],
        [
            InlineKeyboardButton(text = "Toshkent viloyat", callback_data = "toshkentvil"),
        ],
        [
            InlineKeyboardButton(text = "Buxoro shahar", callback_data = "buxoroshah"),
        ],
        [
            InlineKeyboardButton(text = "Buxoro viloyat", callback_data = "buxorovil"),
        ],
        [
            InlineKeyboardButton(text = "Buxoro", callback_data = "toshkentvil"),
        ],


    ],
)


yoqlama= InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="KELDI 🏢 ", callback_data="keldi"),
            InlineKeyboardButton(text="KETDI 🏢", callback_data="ketdi"),

        ],
            [
                InlineKeyboardButton(text="ARIZA 📃", callback_data="ariza"),

             ],

    ],  
)
yoqlama1 = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="KETDI🏢 ", callback_data="ketdi"),

        ],
    ],
)
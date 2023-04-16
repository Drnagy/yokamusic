from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="« اضغط هنا لاضافتي الي مجموعتڪ »",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="« الاوامـر »",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="« الاعـدادات »", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="« اضغط هنا لاضافتي الي مجموعتڪ »",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="« الاوامـر »", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="« 𝐘𝐎𝐊𝐀 | يـوڪــا »", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="« مـطـوري »", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="« الـسـورس »", url=f"https://t.me/INAGYI"
            )
        ],
     ]
    return buttons

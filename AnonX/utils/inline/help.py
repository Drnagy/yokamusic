from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="« الادمـن »",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="« المـالڪـين »",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="« الحـظـر »",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="« الاذاعـة »",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="« حـظر عـام »",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="« ليـرڪـس »",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="« البينـج »",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="« التشـغـيل »",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="« القـوائم »",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="« الفيديـو شـات »",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="« التـهـيئـة »",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="« المـطـورين »",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« الاوامـر »",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

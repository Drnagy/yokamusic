from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« شـخصي »",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="« عـام »", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="« اغـلاق »", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« تـوب 10 »", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="« شـخصي »", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="« عـام »", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="« جـروبات »", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="« رجـوع »", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="« اغـلاق »", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« صـوت »", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="« فـيديو »", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="« رجـوع »", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="« اغـلاق »", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« تـوب 10 »", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="« شـخصي »", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="« عـام »", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="« جـروبات »", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="« رجـوع »", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="« اغـلاق »", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="« رجـوع »",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="« اغـلاق »", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="« حـذف »",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="« رجـوع »",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="« اغـلاق »",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="« اغـلاق »",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

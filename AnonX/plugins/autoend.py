from pyrogram import filters

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import autoend_off, autoend_on
from AnonX.utils.decorators.language import language
from strings.filters import command
# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(
    command(AUTOEND_COMMAND)
    & SUDOERS
)
async def auto_end_stream(client, message):
    usage = "**طريقة الاستخدام:**/n/n» الانهاء التلقائي+[تفعيل-تعطيل]."
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» تم **تفعيل** الانهاء التلقائي بنجاح ✓/n/nـ سيقوم الحساب المساعد بمغادرة المكالمة وانهائها في حالة عدم وجود اشخاص في الاتصال مع ارسال تنبية في الجروب ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» تم **تعطيل** الانهاء التلقائي بنجاح ✓ .")
    else:
        await message.reply_text(usage)

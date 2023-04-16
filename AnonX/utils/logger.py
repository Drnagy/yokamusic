from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**♢ يا هـلا بالغـلا ♢**/n/n»** هناك طلب جديد من:-**/n↤**المستخدم**: {message.from_user.mention}/n↤**يوزره**: @{message.from_user.username}/n↤**ايديه**: {message.from_user.id}/n↤**بجـروب**: {message.chat.title} [{message.chat.id}]/n↤**رابطه**: {chatusername}/n↤**الطلب**: {message.text}/n↤**نوع التشغيل**: {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

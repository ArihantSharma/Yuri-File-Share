#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>× ɢᴏᴅ : <a href='tg://user?id={OWNER_ID}'>🫨 🫨</a>\n× ʜᴇɴᴛᴀɪ ʏᴜɢᴇɴ : @Hentai_Yugen\n× ᴘᴏʀɴʜᴡᴀ ʏᴜɢᴇɴ : @Pornhwa_Yugen\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : @Anime_Yugen\n× ᴍᴀɴɢᴀ ᴄʜᴀɴɴᴇʟ : @Manga_Yugen</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🫠 ᴄʟᴏꜱᴇ!", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
            

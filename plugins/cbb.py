#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, HELP_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Creator: @eren_yeagerattacktitan\nBot: File Sharing Bot\nChannel: @Otaku_Oracle\nSupport: @otaku_oracle_supportgroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data = "start")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_MSG,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data = "start")
                    ]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text = "Use the buttons below to navigate.",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help", callback_data = "help"),
                        InlineKeyboardButton("Close", callback_data = "close")
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

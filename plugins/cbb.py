#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, HELP_MSG, ADMINS, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = "<b>Bot Information</b>\n\nCreator: @eren_yeagerattacktitan\nBot: File Sharing Bot\nChannel: @Otaku_Oracle\nSupport: @otaku_oracle_supportgroup",
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
    elif data == "menu":
        # Check if user is admin
        user_id = query.from_user.id
        if user_id in ADMINS:
            menu_text = """<b>Admin Menu - All Commands</b>

<b>User Commands:</b>
/start - Start the bot
/help - Show help menu

<b>Admin Commands:</b>
/admin - Dashboard
/genlink - Single file link
/batch - Multiple files link
/users - Total users
/broadcast - Send to all
/cancel - Stop operation
/delete - Remove file
/stats - Bot uptime"""
        else:
            menu_text = """<b>User Menu - Available Commands</b>

/start - Start the bot
/help - Show help menu
/cancel - Cancel operations"""
        
        await query.message.edit_text(
            text = menu_text,
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
            text = START_MSG.format(
                first = query.from_user.first_name,
                last = query.from_user.last_name,
                username = None if not query.from_user.username else '@' + query.from_user.username,
                mention = query.from_user.mention,
                id = query.from_user.id
            ),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help", callback_data = "help"),
                        InlineKeyboardButton("Menu", callback_data = "menu")
                    ],
                    [
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

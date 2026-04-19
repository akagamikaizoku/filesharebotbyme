#(©)CodeXBotz




import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from datetime import datetime

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, HELP_MSG, ADMIN_MSG
from helper_func import subscribed, encode, decode, get_messages, get_readable_time, notify_admin_new_user
from database.database import add_user, del_user, full_userbase, present_user




@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
            # Notify admins about the new user
            user_name = message.from_user.username or ""
            user_first_name = message.from_user.first_name or "User"
            await notify_admin_new_user(client, id, user_name, user_first_name)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
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
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

    
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

    
    
@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="<b>Fetching user count...</b>")
    users = await full_userbase()
    await msg.edit(f"<b>Total Users:</b> <code>{len(users)}</code>")

@Bot.on_message(filters.command('help') & filters.private)
async def help_command(client: Client, message: Message):
    await message.reply_text(
        text = HELP_MSG,
        disable_web_page_preview = True,
        quote = True
    )

@Bot.on_message(filters.command('admin') & filters.private & filters.user(ADMINS))
async def admin_dashboard(client: Bot, message: Message):
    users = await full_userbase()
    now = datetime.now()
    delta = now - client.uptime
    uptime = get_readable_time(delta.seconds)
    
    await message.reply_text(
        text = ADMIN_MSG.format(users=len(users), uptime=uptime),
        disable_web_page_preview = True,
        quote = True
    )

@Bot.on_message(filters.command('cancel') & filters.private)
async def cancel_command(client: Client, message: Message):
    try:
        await message.delete()
    except:
        pass
    await message.reply_text("<b>Operation cancelled.</b>", quote=True)

@Bot.on_message(filters.command('delete') & filters.private & filters.user(ADMINS))
async def delete_message(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("<b>Usage:</b> Reply to a forwarded message from the DB channel to delete it.", quote=True)
        return
    
    try:
        replied_msg = message.reply_to_message
        if replied_msg.forward_from_chat and replied_msg.forward_from_chat.id == client.db_channel.id:
            msg_id = replied_msg.forward_from_message_id
            await client.delete_messages(chat_id=client.db_channel.id, message_ids=[msg_id])
            await message.reply_text(f"<b>Deleted</b>\nMessage ID: <code>{msg_id}</code> removed from database.", quote=True)
        else:
            await message.reply_text("<b>Error</b>\nThis message is not from the DB channel.", quote=True)
    except Exception as e:
        await message.reply_text(f"<b>Error:</b> <code>{str(e)}</code>", quote=True)

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<b>Broadcasting message to all users...</b>\n\nThis will take some time.")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b>Broadcast Completed</b>

━━━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Statistics:</b>

👥 Total Users: <code>{total}</code>
✅ Successful: <code>{successful}</code>
❌ Blocked Users: <code>{blocked}</code>
🗑️ Deleted Accounts: <code>{deleted}</code>
⚠️ Unsuccessful: <code>{unsuccessful}</code>

━━━━━━━━━━━━━━━━━━━━━━━━"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

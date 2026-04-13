#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link\n\n(Send /cancel to stop)", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded) | filters.command('cancel')), timeout=60)
        except:
            return
        
        # Check if cancel command was sent
        if first_message.text and first_message.text.startswith('/cancel'):
            await message.reply("<b>Operation cancelled.</b>\nBatch link generation stopped.", quote=True)
            return
        
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link\n\n(Send /cancel to stop)", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded) | filters.command('cancel')), timeout=60)
        except:
            return
        
        # Check if cancel command was sent
        if second_message.text and second_message.text.startswith('/cancel'):
            await message.reply("<b>Operation cancelled.</b>\nBatch link generation stopped.", quote=True)
            return
        
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    
    # Calculate number of files in batch
    if f_msg_id <= s_msg_id:
        file_count = s_msg_id - f_msg_id + 1
    else:
        file_count = f_msg_id - s_msg_id + 1
    
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Batch Link Created</b>\n\n📊 Files Included: <code>{file_count}</code>\n\n<b>Link:</b>\n<code>{link}</code>", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link\n\n(Send /cancel to stop)", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded) | filters.command('cancel')), timeout=60)
        except:
            return
        
        # Check if cancel command was sent
        if channel_message.text and channel_message.text.startswith('/cancel'):
            await message.reply("<b>Operation cancelled.</b>\nLink generation stopped.", quote=True)
            return
        
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("<b>Invalid Message</b>\n\nThis forwarded post is not from your DB Channel or the link is incorrect.\n\nPlease try again.", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Link Generated</b>\n\n<b>Link:</b>\n<code>{link}</code>", quote=True, reply_markup=reply_markup)

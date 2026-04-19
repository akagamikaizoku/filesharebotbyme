# File Sharing Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
</p>

A powerful Telegram bot for storing files and documents with secure shareable links. Users can access files through unique encoded links, and admins can easily manage file distribution with batch processing capabilities.

## Overview

This bot allows you to:
- Upload files to a private Telegram channel
- Generate secure, shareable links for files
- Support batch file sharing (multiple files in one link)
- Notify admins when new users join
- Broadcast messages to all users
- View bot statistics and user count
- Customize messages and settings



## Features

- ✅ Upload files to secure private channel
- ✅ Generate unique shareable links for individual files
- ✅ Batch file sharing (link for multiple files in sequence)
- ✅ Admin notifications for new users
- ✅ Broadcast messages to all users
- ✅ Admin dashboard with statistics
- ✅ MongoDB database integration
- ✅ Fully customizable messages and settings
- ✅ Force subscription channel support
- ✅ File forwarding protection
- ✅ Lightweight and easy to deploy

## Prerequisites

Before you start, ensure you have:

1. **Telegram Bot Token** - Create one from [@BotFather](https://t.me/BotFather)
2. **API Credentials** - Get your API ID and API Hash from [my.telegram.org](https://my.telegram.org)
3. **Private Telegram Channel** - For storing files (bot must be admin with all permissions)
4. **MongoDB Database** - Free tier available at [mongodb.com](https://www.mongodb.com/)
5. **Admin User IDs** - Your Telegram ID and any additional admin IDs

### Pre-Deployment Setup

1. Create a new **private Telegram channel** for file storage
2. Add the bot to the channel as an **admin** with all permissions
3. Get your **channel ID** (forward any message from the channel to [@getmyid_bot](https://t.me/getmyid_bot))
4. (Optional) Create a **Force-Sub channel** for mandatory subscriptions
5. Create a **MongoDB database** and get the connection string

## Installation

### Option 1: Local Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd filesharebotbyme

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
cp .env.example .env

# Edit .env with your configuration
nano .env
# or use your preferred editor

# Run the bot
python main.py
```

### Option 2: Docker Deployment

```bash
docker build -t file-sharing-bot .
docker run -e TG_BOT_TOKEN="YOUR_TOKEN" \
           -e APP_ID="YOUR_APP_ID" \
           -e API_HASH="YOUR_API_HASH" \
           -e CHANNEL_ID="YOUR_CHANNEL_ID" \
           -e OWNER_ID="YOUR_ID" \
           -e DATABASE_URL="YOUR_MONGO_URI" \
           -e ADMINS="ADMIN_IDS" \
           file-sharing-bot
```

## How to Use - Step by Step

### For Regular Users

#### Step 1: Start the Bot
- Send `/start` to the bot
- If force subscription is enabled, join the required channel first

#### Step 2: Access Files
- Open a link shared with you
- The bot will send you the file
- Your chat with the bot will be recorded in the database

### For Admins

#### Step 1: Upload a Single File
1. Send any file (document, photo, video, etc.) to the bot
2. The bot automatically uploads to your DB channel
3. A unique shareable link is generated instantly
4. Share the link with users who need the file

**Example Link:** `https://t.me/your_bot?start=base64_encoded_string`

#### Step 2: Generate Single File Link (`/genlink`)
1. Open your **DB channel** and find the file you want to share
2. **Forward that message** to the bot with quotes
3. Send `/genlink`
4. Wait for bot response
5. The bot will send you the shareable link
6. Copy and share with users

**Alternative:** Instead of forwarding, you can:
- Send the DB channel post **link** directly
- Send `/genlink` 
- The bot generates the link

#### Step 3: Create Batch Links (`/batch`)
For sharing multiple files in one link:

1. Open your **DB channel**
2. Send `/batch` to the bot
3. Bot asks: *"Forward the First Message from DB Channel"*
   - Forward the message of the **first file** you want to include
4. Bot asks: *"Forward the Last Message from DB Channel"*
   - Forward the message of the **last file** you want to include
5. Bot calculates and creates a batch link including all files between first and last
6. Share the generated link - users will receive all files in the range

**Note:** `/batch` creates links for a continuous range of messages from your DB channel

#### Step 4: View Bot Statistics (`/admin`)
- Send `/admin` 
- View total users and bot uptime

#### Step 5: Broadcast Messages (`/broadcast`)
1. **Reply** to any message in the bot chat
2. Send `/broadcast`
3. The message will be sent to all users in the database
4. Bot shows statistics of sent/failed messages

#### Step 6: View Total Users (`/users`)
- Send `/users`
- Bot displays total number of registered users

#### Step 7: Check Bot Uptime (`/stats`)
- Send `/stats`
- View bot uptime and performance

#### Step 8: Cancel Operations (`/cancel`)
- Use this command to stop any ongoing operation
- Works during /batch, /genlink, or /broadcast

#### Step 9: View Help (`/help`)
- Send `/help`
- View all available commands with descriptions

## Environment Variables

Create a `.env` file in the project root with the following variables:

### Required Variables

```env
# Telegram Bot Credentials
TG_BOT_TOKEN=your_bot_token_from_botfather

# Telegram API Credentials (from my.telegram.org)
APP_ID=your_app_id
API_HASH=your_api_hash

# Your Telegram ID (forward any message to @getmyid_bot)
OWNER_ID=your_telegram_id

# Private channel ID for storing files
CHANNEL_ID=-100xxxxxxxxxx

# MongoDB Connection String
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/

# Admin IDs (space-separated)
ADMINS=123456789 987654321
```

### Optional Variables

```env
# Force subscription channel (set to 0 to disable)
FORCE_SUB_CHANNEL=0

# Database name (default: filesharexbot)
DATABASE_NAME=filesharexbot

# Custom welcome message (supports {first}, {username}, {id}, {mention})
START_MESSAGE=Hello {first}!\n\nI'm a File Sharing Bot. Send me files and I'll generate secure shareable links.

# Force subscription message
FORCE_SUB_MESSAGE=You must join to use this bot

# Custom caption for files
CUSTOM_CAPTION=File: {filename}

# Prevent file forwarding (True/False)
PROTECT_CONTENT=False

# Disable channel share button
DISABLE_CHANNEL_BUTTON=False

# Number of bot workers
TG_BOT_WORKERS=4

# Server port
PORT=8080
```

### Message Variables

Available placeholders for custom messages:

- `{first}` - User's first name
- `{last}` - User's last name
- `{id}` - User's ID
- `{username}` - User's username
- `{mention}` - Clickable user mention
- `{filename}` - Document file name (for caption)
- `{uptime}` - Bot uptime (for stats)

## Troubleshooting

### Bot not responding
- Verify bot token is correct
- Check API ID and API Hash from my.telegram.org
- Ensure bot has been added to your DB channel

### Database connection error
- Verify MongoDB connection string is correct
- Check database credentials
- Allow your IP in MongoDB network access settings

### Files not uploading
- Confirm bot is admin in the DB channel with all permissions
- Verify CHANNEL_ID is correct
- Ensure file size is within Telegram's limits (2GB max)

### Links not working
- Verify bot username is correct
- Check if the bot is still running
- Ensure DB channel messages still exist

### Force subscription not working
- Add bot as admin to the force-sub channel
- Give bot "Add Users" permission
- Verify FORCE_SUB_CHANNEL ID is correct

## Dependencies

The bot requires:
- **pyrogram** - Telegram client library
- **TgCrypto** - Encryption support
- **pyromod** - Interactive message handling
- **pymongo** - MongoDB driver
- **aiohttp** - Async HTTP client

All dependencies are listed in `requirements.txt`

## License

This project is licensed under the **GNU General Public License v3.0**.

You are free to:
- ✅ Use this software for any purpose
- ✅ Study how it works and modify it
- ✅ Share it with others
- ✅ Share your modifications

Under the condition that you:
- 📋 Disclose the source code
- 📋 Include a copy of this license
- 📋 Provide the same freedoms to others

For more details, see the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)


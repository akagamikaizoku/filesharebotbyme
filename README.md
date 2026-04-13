# File-sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/CodeXBotz">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/codexbotzsupport">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/CodeXBotz/File-Sharing-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

##

**If you need any more modes in repo or If you find out any bugs, mention in [@codexbotzsupport ](https://www.telegram.dog/codexbotzsupport)**

**Make sure to see [contributing.md](https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/CONTRIBUTING.md) for instructions on contributing to the project!**



### Features
- Fully customizable bot with configurable messages
- Customizable welcome & force-subscription messages
- Batch file sharing (multiple files in one link)
- Single file sharing with unique links
- File deletion capability
- Broadcast messages to all users
- Admin dashboard with statistics
- Admin commands for file management
- MongoDB database integration
- Lightweight and easy to deploy

### Setup Requirements

Before deploying, you need:
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Your API ID and API Hash from [my.telegram.org](https://my.telegram.org)
- A private Telegram channel for storing files
- MongoDB database (free tier available at [mongodb.com](https://www.mongodb.com/))
- Admin permissions in the file storage channel

### Pre-Deployment Checklist

1. Create a new private Telegram channel for file storage
2. Add your bot to the channel with ALL permissions
3. Get your channel ID (forward any message and use `/getmyid` in another bot)
4. Optionally, create a Force-Sub channel and add bot as admin with "Invite Users via Link" permission
5. Create a MongoDB database at [mongodb.com](https://www.mongodb.com/) (free)
6. Get your MongoDB connection string

##
### Installation

#### Quick Deploy on Koyeb (Recommended)

The fastest way to deploy:

1. Fork this repository to your GitHub account
2. Go to [Koyeb Console](https://app.koyeb.com)
3. Click "**Deploy to Koyeb**" button below (you'll need to authenticate with GitHub)
4. Fill in the environment variables (see Variables section)
5. Deploy!

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CodeXBotz/File-Sharing-Bot&branch=main&name=file-sharing-bot)

**Koyeb Setup Steps:**
1. After clicking deploy, authenticate with your GitHub account
2. Select your forked repository
3. In "Environment Variables" section, add all variables from `.env.example`
4. Click "Deploy Service"
5. Wait for deployment to complete

#### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

**Railway Setup:**
1. Click the button above
2. Connect your GitHub account
3. Add all environment variables
4. Deploy

#### Deploy on Heroku (Legacy)
**BEFORE YOU DEPLOY, FORK THE REPO AND CHANGE ITS NAME**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>

#### Deploy on Your VPS/Server
````bash
# Clone the repository
git clone https://github.com/yourusername/File-Sharing-Bot
cd File-Sharing-Bot

# Install dependencies
pip3 install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your configuration
nano .env

# Run the bot
python3 main.py
````

### Commands

**User Commands:**
- `/start` - Start the bot or access files via link
- `/help` - View all available commands
- `/cancel` - Cancel ongoing operations

**Admin Commands:**
- `/admin` - View admin dashboard with statistics
- `/genlink` - Generate a link for a single file (forward a file and use this command)
- `/batch` - Create a link for multiple files (batch processing)
- `/users` - View total number of bot users
- `/broadcast` - Send a message to all users (reply to message + command)
- `/delete` - Delete a file from database (reply with forwarded message)
- `/stats` - Check bot uptime

**How to Add Files:**
1. Simply send any file/document to the bot (as an admin)
2. Bot will upload it to your private channel
3. Bot will generate a shareable link automatically
4. Share the link with whoever needs the file

### Environment Variables

Create a `.env` file or set these environment variables. See `.env.example` for template:

**Required:**
* `TG_BOT_TOKEN` - Bot token from @BotFather
* `APP_ID` - API ID from my.telegram.org
* `API_HASH` - API Hash from my.telegram.org
* `CHANNEL_ID` - Your private file storage channel ID
* `OWNER_ID` - Your Telegram user ID
* `DATABASE_URL` - MongoDB connection string
* `ADMINS` - Space-separated list of admin user IDs

**Optional:**
* `FORCE_SUB_CHANNEL` - Channel ID for force subscription (0 to disable)
* `DATABASE_NAME` - MongoDB database name (default: filesharexbot)
* `START_MESSAGE` - Custom welcome message
* `FORCE_SUB_MESSAGE` - Custom force subscription message
* `CUSTOM_CAPTION` - Custom caption for files
* `PROTECT_CONTENT` - Set True to prevent file forwarding
* `DISABLE_CHANNEL_BUTTON` - Set True to disable channel share button
* `TG_BOT_WORKERS` - Number of bot workers (default: 4)
* `PORT` - Port number (default: 8080)

### Troubleshooting

**Bot not responding:**
- Check if bot token is correct
- Verify API ID and API Hash
- Make sure bot is added to the channel

**Database connection error:**
- Check MongoDB connection string
- Verify database credentials
- Ensure IP whitelist includes your server IP

**Force subscription not working:**
- Add bot to the force sub channel as admin
- Give bot "Invite Users via Link" permission
- Verify channel ID is correct

**File not uploading:**
- Check if bot has permissions in storage channel
- Verify channel ID is correct
- Ensure file size is within Telegram limits
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `DATABASE_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#custom_stats'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime


## Support   
Join Our [Telegram Group](https://www.telegram.dog/codexbotzsupport) For Support/Assistance And Our [Channel](https://www.telegram.dog/codexbotz) For Updates.   
   
Report Bugs, Give Feature Requests There..   

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/CodeXBotz/File-Sharing-Bot/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Star this Repo if you Liked it ⭐⭐⭐**


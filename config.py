#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6519157384:AAHSyUw0WpAaTZY3bCenfLPIRUqvfMEWnrU")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25004026"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c099cac9cb4e8e15398db4dd40342568")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002132173935"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6590244406"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://umoktxy496:IHf8fWyPlLcUwEkx@cluster0.lzqjkxy.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote>ʏᴏᴏ {mention}‼️🥳\nꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋꜱ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ‼️</blockquote>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6590244406 1895356693 6321064549 6907806722").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote>ʏᴏᴜ ᴇxᴘᴇᴄᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴡɪᴛʜᴏᴜᴛ ᴇᴠᴇɴ ᴊᴏɪɴɪɴɢ ᴍʏ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ? 😔</blockquote>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>ʙᴏᴛꜱ ᴜᴘᴛɪᴍᴇ</b>\n{uptime}"
USER_REPLY_TEXT = "<blockquote>ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ, ɪ'ᴍ ʟᴏʏᴀʟ ᴛᴏ ᴍʏ ᴀᴅᴍɪɴꜱ 😤</blockquote>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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

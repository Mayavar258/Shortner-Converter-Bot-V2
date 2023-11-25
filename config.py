# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "1522127"))
API_HASH = os.environ.get("API_HASH", "1252ffe16baf341bfd7236f92df76b0e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6784231545:AAGU7sU_8zgf_jWdfZ0sPxmNEhy9NPzgjUI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1006159057")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "maya")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Mayavan2580:A.M.R.K.S.@maya.vpwb2me.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1006159057")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002117005762")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "ANLINKS_IN") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/0d5e8ce91cb1f64eccfba.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

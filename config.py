import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

class Config:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    STRING_SESSION = os.getenv("STRING_SESSION", "")
    
    # Optional settings
    SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "").split())) if os.getenv("SUDO_USERS") else []
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
    
    # Aesthetic names
    BOT_NAME = "˹ʙʀᴏᴋᴇɴ ꭙ ᴍᴜsɪᴄ˼"

config = Config()

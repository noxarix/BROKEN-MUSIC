import asyncio
import logging
from pyrogram import Client, idle
from BrokenXmusic.core.bot import bot
from BrokenXmusic.core.userbot import userbot
from BrokenXmusic.core.calls import call
from config import config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

async def init():
    print("Starting ˹ʙʀᴏᴋᴇɴ ꭙ ᴍᴜsɪᴄ˼...")

    # Start Bot
    await bot.start()
    print("Bot Started!")

    # Start Userbot
    await userbot.start()
    print("Userbot Started!")

    # Start PyTgCalls
    await call.start()
    print("PyTgCalls Started!")

    print("˹ʙʀᴏᴋᴇɴ ꭙ ᴍᴜsɪᴄ˼ is now active!")
    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())

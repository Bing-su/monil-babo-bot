import os
from pathlib import Path

import discord
from dotenv import load_dotenv
from loguru import logger

if os.name != "nt":
    import uvloop

    uvloop.install()

load_dotenv()

bot = discord.Bot(intents=discord.Intents.default(), debug_guilds=[460038871279861761])
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_connect():
    logger.info("연결됐어!")


@bot.event
async def on_ready():
    logger.info("모닐 바보봇 준비됐어!")


@bot.event
async def on_disconnect():
    logger.info("끊겼어!")


# add Cogs
for cog in Path("cogs").rglob("*.py"):
    if not cog.name.startswith("_"):
        cog_name = f"cogs.{cog.stem}"
        bot.load_extension(cog_name)
        logger.info(f"{cog_name} 불러왔어!")


bot.run(TOKEN)

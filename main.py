import os
from pathlib import Path

import discord
from dotenv import load_dotenv
from loguru import logger

if os.name != "nt":
    import uvloop

    uvloop.install()

load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)
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


@bot.slash_command(name="생존확인")
async def ping(ctx: discord.ApplicationContext):
    logger.info(f"{ctx.author}가 내가 살아있는지 궁금한가봐!")
    await ctx.respond("나 살아있어!")


# add Cogs
for cog in Path("cogs").rglob("*.py"):
    if not cog.name.startswith("_"):
        cog_name = f"cogs.{cog.stem}"
        bot.load_extension(cog_name)
        logger.info(f"{cog_name} 불러왔어!")


bot.run(TOKEN)

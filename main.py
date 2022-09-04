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
intents.message_content = True

if "DEBUG" in os.environ:
    bot = discord.Bot(
        intents=intents,
        debug_guilds=[460038871279861761],
    )
    logger.info("디버그 모드야!")
else:
    bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    logger.info("모닐 바보봇 준비됐어!")


@bot.slash_command(name="생존확인")
async def ping(ctx: discord.ApplicationContext):
    "생존확인"
    logger.info(f"{ctx.author}가 내가 살아있는지 궁금한가봐! {bot.latency:.4f}s")
    await ctx.respond(f"나 살아있어! `{bot.latency:.4f}s`")


# add Cogs
for cog in Path("cogs").rglob("*.py"):
    if not cog.name.startswith("_"):
        cog_name = f"cogs.{cog.stem}"
        bot.load_extension(cog_name)
        logger.info(f"{cog_name} 불러왔어!")


# run
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)

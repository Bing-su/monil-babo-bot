import os

import discord
from discord import InteractionContext
from dotenv import load_dotenv

if os.name != "nt":
    import uvloop

    uvloop.install()

load_dotenv()

bot = discord.Bot(intents=discord.Intents.default())
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print("봇이 준비되었습니다!")


@bot.slash_command(name="바보")
async def slash_babo(
    ctx: InteractionContext,
    user: discord.Option(discord.Member, description="이 사람이 바보야!"),
):
    "바보바보!"
    await ctx.respond(f"{user.mention} 바보!")


@bot.message_command(name="바보")
async def message_babo(ctx: InteractionContext, message: discord.Message):
    await ctx.respond(f"{message.author.mention} 바보!")


@bot.user_command(name="바보")
async def user_babo(ctx: InteractionContext, user: discord.Member):
    await ctx.respond(f"{user.mention} 바보!")


bot.run(TOKEN)

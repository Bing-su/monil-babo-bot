import discord
from discord import ApplicationContext, Option
from discord.ext import commands
from loguru import logger


class Babo(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name="바보")
    async def slash_babo(
        self,
        ctx: ApplicationContext,
        user: Option(discord.Member, description="이 사람이 바보야!"),
    ):
        "바보바보!"
        logger.info(f"slash_babo: {ctx.author}가 {user}를 바보로 지정했어!")
        await ctx.respond(f"{user.mention} 바보!")

    @commands.message_command(name="바보2")
    async def message_babo(self, ctx: ApplicationContext, message: discord.Message):
        logger.info(f"message_babo: {ctx.author}가 {message.author}를 바보로 지정했어!")
        await ctx.respond(f"{message.author.mention} 바보!")

    @commands.user_command(name="바보3")
    async def user_babo(self, ctx: ApplicationContext, user: discord.Member):
        logger.info(f"user_babo: {ctx.author}가 {user}를 바보로 지정했어!")
        await ctx.respond(f"{user.mention} 바보!")

    @commands.slash_command(name="똑똑해")
    async def slash_ddokddokhae(
        self,
        ctx: ApplicationContext,
        user: Option(discord.Member, description="너 좀 치는데?"),
    ):
        "똑똑해!"
        await ctx.respond(f"{user.mention} 똑또캐!")

    @commands.message_command(name="똑똑해2")
    async def message_ddokddokhae(
        self, ctx: ApplicationContext, message: discord.Message
    ):
        await ctx.respond(f"{message.author.mention} 똑또캐!")

    @commands.user_command(name="똑똑해3")
    async def user_ddokddokhae(self, ctx: ApplicationContext, user: discord.Member):
        await ctx.respond(f"{user.mention} 똑또캐!")


def setup(bot: discord.Bot):
    bot.add_cog(Babo(bot))

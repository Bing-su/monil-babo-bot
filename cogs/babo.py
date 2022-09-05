import discord
from discord import ApplicationContext, Cog, Option, commands


class Babo(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    # --- 바보 ---
    @commands.slash_command(name="바보")
    async def slash_babo(
        self,
        ctx: ApplicationContext,
        user: Option(discord.Member, name="바보", description="이 사람이 바보야!"),
    ):
        "바보바보!"
        await ctx.respond(f"{user.mention} 바보!")

    @commands.user_command(name="바보")
    async def user_babo(self, ctx: ApplicationContext, user: discord.Member):
        await ctx.respond(f"{user.mention} 바보!")

    @commands.message_command(name="바보")
    async def message_babo(self, ctx: ApplicationContext, message: discord.Message):
        await ctx.delete()
        await message.reply(f"{message.author.mention} 바보!")

    # --- 똑똑해 ---
    @commands.slash_command(name="똑똑해")
    async def slash_ddokddokhae(
        self,
        ctx: ApplicationContext,
        user: Option(discord.Member, name="똑똑이", description="너 좀 치는데?"),
    ):
        "똑똑해!"
        await ctx.respond(f"{user.mention} 똑또캐!")

    @commands.user_command(name="똑똑해")
    async def user_ddokddokhae(self, ctx: ApplicationContext, user: discord.Member):
        await ctx.respond(f"{user.mention} 똑또캐!")

    @commands.message_command(name="똑똑해")
    async def message_ddokddokhae(
        self, ctx: ApplicationContext, message: discord.Message
    ):
        await ctx.delete()
        await message.reply(f"{message.author.mention} 똑또캐!")


def setup(bot: discord.Bot):
    bot.add_cog(Babo(bot))

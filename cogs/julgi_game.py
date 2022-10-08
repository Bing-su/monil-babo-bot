import discord
from discord import ApplicationContext, Cog, Option, commands
from julgi import game


class JulgiGame(Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name="줄기게임")
    async def slash_julgi_game(
        self,
        ctx: ApplicationContext,
        user1: Option(str, name="유저1", description="첫 번째 유저야!"),
        user2: Option(str, name="유저2", description="두 번째 유저야!"),
        seed: Option(str, name="시드", description="시드는 옵션이야!") = "",
    ):
        "줄기 게임!"
        result_text = game(user1, user2, seed, return_as_list=False)

        result = "```py\n" + result_text + "\n```"
        await ctx.respond(result)


def setup(bot: discord.Bot):
    bot.add_cog(JulgiGame(bot))

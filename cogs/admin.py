from discord.ext import commands
from checks import is_admin

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shutdown")
    @is_admin()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down.")
        await self.bot.close()

def setup(bot):
    bot.add_cog(AdminCog(bot))

from discord.ext import commands
from utils.checks import is_admin

class AdminCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="shutdown")
  @is_admin()
  async def shutdown(self, ctx: commands.Context):
    await ctx.send("Shutting down.")
    await self.bot.close()

  @commands.command(name="scan_r2")
  @is_admin
  async def scan_r2(self, ctx: commands.Context):
    

async def setup(bot):
  await bot.add_cog(AdminCog(bot))

from discord.ext import commands
from utils.checks import is_admin
from services.firebase_service import get_video_metadata, save_video_metadata

class AdminCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="shutdown")
  @is_admin()
  async def shutdown(self, ctx: commands.Context):
    await ctx.send("Shutting down.")
    await self.bot.close()

  @commands.command(name="add_tag")
  @is_admin()
  async def add_tag(self, meme_url: str, tag: str , ctx:commands.Context):
    if not isinstance(tag, str):
      ctx.send("Sorry, but tags are in wrong type. Use as a delimeter ', '!")
      return
    
    response = await get_video_metadata(meme_url)
    if response is None:
      ctx.send("Sorry, no such meme were found!")
      return
    
    response.
    

async def setup(bot):
  await bot.add_cog(AdminCog(bot))

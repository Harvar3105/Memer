from discord.ext import commands
from utils.checks import is_admin, is_reply_to_bot
from repos.firebase_service import get_video_metadata, save_video_metadata
from domain.Metadata import Metadata
from utils.parsers import parse_tags_from_st
from domain.Metadata import Tag

class AdminCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="shutdown", description="Shut down bot.")
  @is_admin()
  async def shutdown(self, ctx: commands.Context):
    await ctx.send("Shutting down 📛")
    await self.bot.close()

  @commands.command(name="add_tags")
  @is_admin()
  async def add_tags(self, meme_key: str, tags: str , ctx:commands.Context):
    if not isinstance(tags, str):
      await ctx.send("Sorry, but tags are in wrong type. Use as a delimeter ', '!")
      return
    
    response: Metadata = await get_video_metadata(meme_key)
    if response is None:
      await ctx.send("Sorry, no such meme were found!")
      return
    
    taglist = parse_tags_from_st(tags)
    response.tags.extend(taglist)
    
    await save_video_metadata(response)
    await ctx.send("✅Tag added!")

  @commands.command(name="add_tags_reply")
  @is_admin()
  @is_reply_to_bot()
  async def add_tags_reply(self, ctx:commands.Context, replied_message_content: str, tags: str):
    parts = tags.split()
    if len(parts) < 1:
      await ctx.send("Sorry, I couldn't find the meme key in the replied message.")
      return

    meme_key = replied_message_content # Later Get key from masked url

    if not isinstance(tags, str):
      await ctx.send("Sorry, but tags are in wrong type. Use as a delimeter ', '!")
      return
    
    response: Metadata = await get_video_metadata(meme_key)
    if response is None:
      await ctx.send("Sorry, no such meme were found!")
      return
    
    taglist = parse_tags_from_st(tags)
    response.tags.extend(taglist)
    
    await save_video_metadata(response)
    await ctx.send("✅Tag added!")

  @commands.command(name="list_tags", description="List all available tags.")
  @is_admin()
  async def list_tags(self, ctx: commands.Context):
    tag_dict = {tag.name: tag.value for tag in Tag}
    tag_str = ",\n".join(f"{k}  =  {v}" for k, v in tag_dict.items())
    await ctx.send(tag_str)


async def setup(bot):
  await bot.add_cog(AdminCog(bot))

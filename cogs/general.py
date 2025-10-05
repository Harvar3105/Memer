from discord.ext import commands
import random
from repos.r2_service import list_files, generate_presigned_url
from utils.config import MEME_URL_EXPIRES_IN_SECONDS
from utils.senders import send_masked

class GeneralCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
    await ctx.send("Pong! 🏓")

  @commands.command(name="r_meme", description="Get random meme.")
  async def meme(self, ctx: commands.Context):
    memes = await list_files()

    if not memes or memes.count == 0:
      await ctx.send("No memes available 😢")
      return

    chosen_one = random.choice(memes)
    presigned_url = await generate_presigned_url(chosen_one.key, MEME_URL_EXPIRES_IN_SECONDS)
    await send_masked(source=ctx, presigned_url=presigned_url, mask=f"**MEME**: {chosen_one.key}")

async def setup(bot):
  await bot.add_cog(GeneralCog(bot))

import discord
from discord.ext import commands
from discord import app_commands
import random
from services.r2_service import list_files, generate_presigned_url
from utils.config import MEME_URL_EXPIRES_IN_SECONDS

class GeneralCog(commands.Cog):
  MEMES_FOLDER = ""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
    await ctx.send("Pong! 🏓")

  # Later add connectivity to DBs test
  @commands.command(name="test")
  async def test(self, ctx: commands.Context):
    await ctx.send("Bot is operative!")
    return

  # Example of slash command
  @app_commands.command(name="ping", description="Answears Pong!")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")

  @commands.command(name="r_number", description="Gets random nuber between 2 inclusive values")
  async def r_number(self, ctx: commands.Context, min: int, max: int):
    await ctx.send(random.randint(min, max))
    return

  @commands.command(name="r_meme")
  async def meme(self, ctx: commands.Context):
    memes_keys = []
    for meme in await list_files():
      memes_keys.append(meme.key)

    if not memes_keys or memes_keys.count == 0:
      await ctx.send("No memes available 😢")
      return

    chosen_one = random.choice(memes_keys)
    presigned_url = await generate_presigned_url(chosen_one, MEME_URL_EXPIRES_IN_SECONDS)
    await ctx.send(presigned_url)

async def setup(bot):
  await bot.add_cog(GeneralCog(bot))

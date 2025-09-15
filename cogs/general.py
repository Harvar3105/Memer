import discord
from discord.ext import commands
from discord import app_commands
import random
from services.r2_service import list_files, get_file_url

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
    memes = []
    for key in await list_files():
      memes.append(get_file_url(key))

    if not memes or memes.count == 0:
      await ctx.send("No memes available 😢")
      return

    meme = random.choice(memes)
    await ctx.send(meme)

async def setup(bot):
  await bot.add_cog(GeneralCog(bot))

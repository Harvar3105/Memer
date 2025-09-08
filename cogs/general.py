import discord
from discord.ext import commands
from discord import app_commands
import random
import os

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
    files = os.listdir(self.MEMES_FOLDER)
    if not files:
      await ctx.send("No memes available 😢")
      return

    file = random.choice(files)
    filepath = os.path.join(self.MEMES_FOLDER, file)
    await ctx.send(file=discord.File(filepath))

async def setup(bot):
  await bot.add_cog(GeneralCog(bot))

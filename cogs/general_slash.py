import random
import discord
from discord import app_commands
from discord.ext import commands

from repos.r2_service import generate_presigned_url, list_files
from utils.config import MEME_URL_EXPIRES_IN_SECONDS
from utils.senders import send_masked

class GeneralCogSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="ping", description="Answears Pong!")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")

  @app_commands.command(name="r_meme", description="Get random meme.")
  async def meme(self, interaction: discord.Interaction):
    memes = await list_files()

    if not memes or memes.count == 0:
      await interaction.response.send_message("No memes available 😢")
      return

    chosen_one = random.choice(memes)
    presigned_url = await generate_presigned_url(chosen_one.key, MEME_URL_EXPIRES_IN_SECONDS)
    await send_masked(source=interaction, presigned_url=presigned_url)

async def setup(bot):
  await bot.add_cog(GeneralCogSlash(bot))
import discord
from discord import app_commands

class GeneralCogSlash():
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="ping", description="Answears Pong!")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")

  @app_commands.command(name="help")
  async def help(self, interaction: discord.Interaction):
    await interaction.response.send_message("""
    Prefix is '!' or '/'
    Commands:
    help    -   show list of available commands
    ping    -   test if bot currently listening
    """)

async def setup(bot):
  await bot.add_cog(GeneralCogSlash(bot))
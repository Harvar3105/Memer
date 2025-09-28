import discord
from discord import app_commands

from utils.checks import is_admin

class AdminCogSlash():
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="shutdown")
  @is_admin()
  async def shutdown(self, interaction: discord.Interaction):
    await interaction.response.send_message("Shutting down 📛")
    await self.bot.close()

async def setup(bot):
  await bot.add_cog(AdminCogSlash(bot))
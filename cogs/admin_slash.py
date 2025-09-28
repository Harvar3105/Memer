import discord
from discord import app_commands
from discord.ext import commands

from domain.Metadata import Tag
from utils.checks import is_admin

class AdminCogSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="shutdown", description="Shut down bot.")
  @is_admin()
  async def shutdown(self, interaction: discord.Interaction):
    await interaction.response.send_message("Shutting down 📛")
    await self.bot.close()

  @app_commands.command(name="list_tags", description="List all available tags.")
  @is_admin()
  async def list_tags(self, interaction: discord.Interaction):
    tag_dict = {tag.name: tag.value for tag in Tag}
    tag_str = ",\n".join(f"{k}  =  {v}" for k, v in tag_dict.items())
    await interaction.response.send_message(tag_str)

async def setup(bot):
  await bot.add_cog(AdminCogSlash(bot))
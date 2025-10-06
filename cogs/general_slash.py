import asyncio
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
  
  @app_commands.command(name="react_clown", description="Set clown emoji to specified user messages. Max: 100 messages.")
  async def react_clown(self, ctx: commands.Context, user: str, amount: int = 1, max_timeout: int = 300):
    if amount < 1 or amount > 100:
      await ctx.send("Amount must be between 1 and 100.")
      return

    try:
      member = await commands.MemberConverter().convert(ctx, user)
    except commands.BadArgument:
      await ctx.send("Invalid user. Please mention the user or provide a valid user ID.")
      return

    def check(message):
      return message.author == member and message.channel == ctx.channel

    await ctx.send(f"Listening to messages from {member.mention} for the next {amount} messages...")

    reacted_count = 0
    while reacted_count < amount:
      try:
        message = await self.bot.wait_for('message', check=check, timeout=max_timeout)
        await message.add_reaction("🤡")
        reacted_count += 1
      except asyncio.TimeoutError:
        await ctx.send("Timeout reached. Stopping listening for messages.")
        break

    await ctx.send(f"Finished reacting to {reacted_count} messages from {member.mention}.")

async def setup(bot):
  await bot.add_cog(GeneralCogSlash(bot))
import discord
from discord.ext import commands
import asyncio
import os
from utils.config import DISCORD_BOT_TOKEN, PREFIX
from services.memer_service import test_all_connections, sync_manually_added_memes

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync();
  print(f"[✅] Logged in as {bot.user}\nStarting db analysis and sync")
  
  await sync_manually_added_memes()

@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  
  if message.reference and isinstance(message.reference.resolved, discord.Message):
      replied_message = message.reference.resolved

      if replied_message.author == bot.user:
          await message.channel.send(f"{message.author.mention}, you replied to my message!")

  await bot.process_commands(message)


async def main():
  async with bot:
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py") and filename != "__init__.py":
        await bot.load_extension(f"cogs.{filename[:-3]}")
    await bot.start(DISCORD_BOT_TOKEN)

asyncio.run(main())


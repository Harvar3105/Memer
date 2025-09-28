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



async def main():
  async with bot:
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py") and filename != "__init__.py":
        await bot.load_extension(f"cogs.{filename[:-3]}")
    await bot.start(DISCORD_BOT_TOKEN)

asyncio.run(main())


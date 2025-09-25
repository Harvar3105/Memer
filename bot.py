import discord
from discord.ext import commands
import asyncio
import os
from services.r2_service import list_files, get_file_url
from services.firebase_service import save_video_metadata, get_video_metadata, exists
from domain.Metadata import Metadata, Tag
from utils.config import DISCORD_BOT_TOKEN, PREFIX

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync();
  print(f"[✅] Logged in as {bot.user}\nStarting db analysis and sync")

  manually_added_count = 0
  for meme in await list_files():
    if not await exists(meme.key):
      meme.tags=[Tag.UNTAGGED]
      meme.created_at = meme.updated_at # If meme never existed in firestore, then its last appearence in r2 concidered as creation date
      await save_video_metadata(meme)
      manually_added_count += 1
      print(f"[✔] Detected a new meme\nURL: {meme.url}\n")

  print(f"\n++++++++++\n🎉Sync completed!\nDetected {manually_added_count} new manually added memes!\n++++++++++\n")


async def main():
  async with bot:
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py") and filename != "__init__.py":
        await bot.load_extension(f"cogs.{filename[:-3]}")
    await bot.start(DISCORD_BOT_TOKEN)

asyncio.run(main())


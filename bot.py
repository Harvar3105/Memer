import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from services.r2_service import list_files, get_file_url
from services.firebase_service import save_video_metadata, get_video_metadata, exists
from domain.Metadata import Metadata, Tag

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync();
  print(f"[✅] Logged in as {bot.user}\nStarting db analysis and sync")

  memes = await list_files()
  print(f"Listed files {memes}")

  for meme in memes:
    url = get_file_url(meme)
    if not await exists(url):
        await save_video_metadata(Metadata(key=url, tags=[Tag.UNTAGGED]))
        print(f"[✔] Detected a new meme\nURL: {url}\n")

  print("🎉Sync completed!")

# @bot.event
# async def on_ready():
#   await bot.tree.sync()
#   print(f"[✅] Logged in as {bot.user}\nStarting db analysis and sync")

#   bot.loop.create_task(_sync_memes_background())

# async def _sync_memes_background():
#   try:
#     try:
#       memes = await asyncio.wait_for(asyncio.to_thread(list_files), timeout=30)
#     except asyncio.TimeoutError:
#       print("[!] list_files() timed out")
#       return
#     except Exception as e:
#       print("[!] list_files() failed:", e)
#       return

#     if not memes:
#       print("[i] No memes found in bucket.")
#       print("🎉 Sync completed!")
#       return

#     total = len(memes)
#     for i, meme in enumerate(memes, start=1):
#       print(f"[{i}/{total}] processing: {meme}")
#       url = get_file_url(meme)

#       try:
#         exists_flag = await asyncio.wait_for(asyncio.to_thread(exists, url), timeout=6)
#       except asyncio.TimeoutError:
#         print(f"[!] exists() timed out for {url}; skipping")
#         continue
#       except Exception as e:
#         print(f"[!] exists() error for {url}: {e}; skipping")
#         continue

#       if not exists_flag:
#         meta = Metadata(key=url, tags=[Tag.UNTAGGED])
#         try:
#           await asyncio.wait_for(asyncio.to_thread(save_video_metadata, meta), timeout=10)
#           print(f"[✔] Detected a new meme\nURL: {url}\n")
#         except asyncio.TimeoutError:
#           print(f"[!] save_video_metadata() timed out for {url}")
#         except Exception as e:
#           print(f"[!] save_video_metadata() failed for {url}: {e}")

#     print("🎉 Sync completed!")
#   except Exception as e:
#     print("Unexpected error in sync:", e)

async def main():
    async with bot:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.start(TOKEN)

asyncio.run(main())

# bot.run(TOKEN)


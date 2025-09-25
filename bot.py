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
    print(f"Meme: {meme}")
    if not await exists(meme.url):
        # await save_video_metadata(Metadata(key=meme.url, tags=[Tag.UNTAGGED]))
        print(f"[✔] Detected a new meme\nURL: {meme.url}\n")

  print("🎉Sync completed!")


async def main():
    async with bot:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.start(TOKEN)

asyncio.run(main())

# bot.run(TOKEN)


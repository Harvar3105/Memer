import discord
from discord.ext import commands
from domain.Metadata import Metadata
from enum import Enum
from utils.config import MEME_URL_EXPIRES_IN_SECONDS
from utils.time_parsers import parse_secons_to_text

async def send_embed(ctx: commands.Context, presigned_url: str, meme: Metadata, title: str = "MEME"):
  try:
    await ctx.send(embed=discord.Embed(
      title=title,
      description=", ".join([tag.value if isinstance(tag, Enum) else tag for tag in meme.tags]),
      color=discord.Color.blue(),
      url=presigned_url
    ))
  except Exception as e:
    print("Error in test_connection:", e)
    import traceback
    traceback.print_exc()

async def send_masked(ctx: commands.Context, presigned_url: str, mask: str = "MEME"):
  await ctx.send(content=f"[{mask}\n{parse_secons_to_text(MEME_URL_EXPIRES_IN_SECONDS)}]({presigned_url})")
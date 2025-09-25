from discord.ext import commands
from utils.config import ADMIN_IDS

def is_admin():
  async def predicate(ctx: commands.Context):
    return f"{ctx.author.id}" in ADMIN_IDS
  return commands.check(predicate)

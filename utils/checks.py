from discord.ext import commands
from utils.config import ADMIN_IDS
from functools import wraps


def is_admin():
  async def predicate(ctx: commands.Context):
    return f"{ctx.author.id}" in ADMIN_IDS
  return commands.check(predicate)

from functools import wraps

def is_reply_to_bot():
    def predicate(func):
        @wraps(func)
        async def wrapper(self, ctx: commands.Context, *args, **kwargs):
            ref = ctx.message.reference
            if not ref or not ref.resolved:
                await ctx.send("You must reply to a bot message to use this command.")
                return
            replied_message = ref.resolved
            if not replied_message.author.bot:
                await ctx.send("You must reply to a bot message to use this command.")
                return
            return await func(self, ctx, replied_message.content, *args, **kwargs)
        return wrapper
    return predicate
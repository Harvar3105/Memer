from discord.ext import commands
from utils.config import ADMIN_IDS
from functools import wraps


def is_admin():
  async def predicate(ctx: commands.Context):
    return f"{ctx.author.id}" in ADMIN_IDS
  return commands.check(predicate)

from functools import wraps

def is_reply_to_bot():
	def predicate(ctx: commands.Context):
		ref = ctx.message.reference
		if not ref or not ref.resolved:
			raise commands.CheckFailure("You must reply to a bot message to use this command.")
		if not getattr(ref.resolved.author, "bot", False):
			raise commands.CheckFailure("You must reply to a bot message to use this command.")
		return True
	return commands.check(predicate)
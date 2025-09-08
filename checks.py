from discord.ext import commands

ADMIN_IDS = [123456789012345678, 987654321098765432]  # user IDs

def is_admin():
    async def predicate(ctx: commands.Context):
        return ctx.author.id in ADMIN_IDS
    return commands.check(predicate)

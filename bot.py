import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"[✅] Logged in as {bot.user}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)


# import discord
# import os
# import random
# from dotenv import load_dotenv
# from discord.ext import commands


# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix="!", intents=intents)

# load_dotenv()
# TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# MEMES_FOLDER = "memes"

# @bot.event
# async def on_ready():
# 	await bot.tree.sync()
# 	print(f"Bot {bot.user} start!")

# @bot.command()
# async def ping(ctx: commands.Context):
#     await ctx.send("Pong! 🏓")

# # Later add connectivity to DBs test
# @bot.command(name="test")
# async def test(ctx: commands.Context):
# 	await ctx.send("Bot is operative!")
# 	return

# # Example of slash command
# @bot.tree.command(name="ping", description="Answears Pong!")
# async def ping(interaction: discord.Interaction):
#     await interaction.response.send_message("Pong! 🏓")

# @bot.command(name="r_number", description="Gets random nuber between 2 inclusive values")
# async def r_number(ctx: commands.Context, min: int, max: int):
# 	await ctx.send(random.randint(min, max))
# 	return

# @bot.command(name="r_meme")
# async def meme(ctx: commands.Context):
# 	files = os.listdir(MEMES_FOLDER)
# 	if not files:
# 		await ctx.send("No memes available 😢")
# 		return

# 	file = random.choice(files)
# 	filepath = os.path.join(MEMES_FOLDER, file)
# 	await ctx.send(file=discord.File(filepath))

# # Launch
# bot.run(TOKEN)

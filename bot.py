import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

MEMES_FOLDER = "memes"

@bot.event
async def on_ready():
	await bot.tree.sync()
	print(f"Bot {bot.user} start!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Later add connectivity to DBs test
@bot.command(name="test")
async def test(ctx):
	await ctx.send("Bot is operative!")
	return

# Example of slash command
@bot.tree.command(name="ping", description="Answears Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")

@bot.command(name="r_meme")
async def meme(ctx):
	files = os.listdir(MEMES_FOLDER)
	if not files:
		await ctx.send("No memes available 😢")
		return

	file = random.choice(files)
	filepath = os.path.join(MEMES_FOLDER, file)
	await ctx.send(file=discord.File(filepath))

# Launch
bot.run(TOKEN)

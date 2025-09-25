from dotenv import load_dotenv
import os

load_dotenv()


PREFIX="!"
MEME_URL_EXPIRES_IN_SECONDS=3600
OWNERS_DISCORD_ID=os.getenv("OWNERS_DISCORD_ID")
ADMIN_IDS=[OWNERS_DISCORD_ID]


R2_ENDPOINT = os.getenv("R2_ENDPOINT")
R2_BUCKET = os.getenv("R2_BUCKET")
R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
R2_ACCOUNT_ID=os.getenv("R2_ACCOUNT_ID")
R2_TOKEN=os.getenv("R2_TOKEN")

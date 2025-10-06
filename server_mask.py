import threading
import os
from flask import Flask
from bot import start_handler
from utils.config import SERVER_MASK_PORT

app = Flask(__name__)

@app.route("/")
def home():
	return "Bot is running!\nTry pinging it with ping command ore check its slash commands!"

def run_flask():
	if SERVER_MASK_PORT is None:
		SERVER_MASK_PORT = '5000'
	app.run(host="0.0.0.0", port=int(SERVER_MASK_PORT))

if __name__ == "__main__":
	threading.Thread(target=run_flask).start()
	start_handler()

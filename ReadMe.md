# Memer 🎭

Memer is a Discord bot for sending random memes to users in Discord servers.  
It uses **Cloudflare R2 Storage** and **Firebase Firestore** for storing data.

---

## ✨ Features Implemented
- 🎲 Send random memes to users  
- 👑 Admin recognition  
- ⏹ Shut down the bot directly from Discord chat  
- 🏷 Show a list of available tags  

---

## 🚧 Planned Features
- ➕ Add tags by specifying a meme name  
- ➕ Add tags by replying to a meme  
- 📤 Upload memes directly through a Discord channel (TBD)  
- 🔀 Show random meme by tag  
- 📑 Show all memes by tag (with pagination)  
- 📑 Show all memes without a tag filter  
- ❌ Remove tags by specifying a meme name  
- ❌ Remove tags by replying to a meme  

---

## ⚙️ Configuration Roadmap
- 💾 Save configuration in a JSON file  
- 📖 Load configuration from a JSON file (with environment variables as priority)  
- 🔧 Configure the bot directly through Discord chat with JSON persistence  

---

## 🔄 Maintenance & Deployment
- 🔁 Reload bot without restarting manually  
- ☁️ Deploy to a simple hosting service  

---

## 📌 Tech Stack
- **Python 3.13+**  
- **discord.py** (slash commands + prefix commands)  
- **Cloudflare R2** (for file storage)  
- **Firebase Firestore** (for metadata and tags)  

---

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/your-username/memer.git
cd memer

# Install dependencies
pip install -r requirements.txt

# Set environment variables (example for Linux/macOS)
export DISCORD_TOKEN="your-bot-token"
export R2_ACCESS_KEY="your-access-key"
export R2_SECRET_KEY="your-secret-key"
export R2_ENDPOINT="https://your-r2-endpoint"
export R2_BUCKET="your-r2-bucket"
export FIREBASE_CREDENTIALS="path-to-serviceAccount.json"

# Run the bot
python main.py

from pyrogram import Client, filters

API_ID = 31994981         # ← paste your api_id
API_HASH = "f311360d4f98f5745f0fee9c65f6226c"
BOT_TOKEN = "8692638174:AAE7B9rr3KwNauM60uxe7W_fR3yfwb_Dj5w" # ← paste token from BotFather

app = Client("public_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🚀 Send me any file and I will store it!")

@app.on_message(filters.private)
async def save_files(client, message):
    if message.document or message.video or message.photo or message.audio:
        await message.reply("✅ File saved successfully!")

app.run()
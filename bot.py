import os
from telethon import TelegramClient, events
from decouple import config

API_ID = int(config("API_ID"))
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SUDO_USERS = list(map(int, config("SUDO_USER", default="").split()))

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.sender_id not in SUDO_USERS:
        return
    await event.respond("🤖 Bot is active and running!")

@bot.on(events.NewMessage(pattern="/broadcast"))
async def broadcast(event):
    if event.sender_id not in SUDO_USERS:
        return
    if not event.is_reply:
        return await event.reply("Reply to a message to broadcast.")
    msg = await event.get_reply_message()
    count = 0
    async for user in bot.iter_participants(event.chat_id):
        try:
            await bot.send_message(user.id, msg)
            count += 1
        except:
            pass
    await event.reply(f"✅ Broadcast sent to {count} users.")

print("Bot is running...")
bot.run_until_disconnected()

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

app = Client(
    "StickerIdBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
 
   
START_TEXT = """
Hai {},
Am Sticker id Finder Bot
I can Find I'd of an sticker. Just send me a sticker and reply it with /StickerId command i would provide its I'd. . 
"""
    
@app.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code📕', url='https://github.com/JinnSulthan/Stickerid'), 
        InlineKeyboardButton('CHANNEL📕', url=f"https://telegram.me/{Config.CHANNEL}")
        ]]
    )



@app.on_message(filters.command("stickerid") & (filters.private | filters.group))
async def stickers(bot, message):
    if message.reply_to_message and message.reply_to_message.sticker:
        await message.reply(
            f"<b>Your Requested Sticker's ID is:</b> <code>{message.reply_to_message.sticker.file_id}</code>",
            quote=True
        )
    elif message.reply_to_message and not message.reply_to_message.sticker:
        await message.reply("Oops! The replied message is not a sticker.")
    else:
        await message.reply("Are you challenging me!\n reply to a sticker instead.")

Bot.run()

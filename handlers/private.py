from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [𝙍𝙮𝙖𝙣 𝙊𝙥](https://t.me/RYAN_HERE)

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                ,[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/COLONY_OF_WEIRDOS_2"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/RYAN_OP_MUSIC_BOT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/VENOM_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**νєиσм ᴍᴜsɪᴄ jinda hai abhi**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/RYAN_OP_MUSIC_BOT")
                ]
            ]
        )
   )



# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks ยฉ @Dr_Asad_Ali ยฉ Rocks
# Owner Asad + Harshit
# ๐เผ _๐ก๐พย Cโค๐๐ข_ินีินิบ เผ๐ต๐ฐ ใUsแดส_แดษชแดแดใ

import logging
from config import BOT_USERNAME
from rocksdriver.filters import command, other_filters
from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("๐๐ ๐8๐ผ๐๐ผ๐ ๐ฆโฝโโโ๐8โ", url=f"https://t.me/U_Y_H"),
                    InlineKeyboardButton("๐๐๐๐๐", url=f"https://t.me/J_G_A"),
                ],
                [
                    InlineKeyboardButton(
                        "- Channel", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    try:
        if len(message.command) < 2:
            await message.reply_text("/search **ษดแดแดแด sแดษดษข ษดแดแดแด !**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("๐ **Searching...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"๐ฎ **Neam:** __{results[i]['title']}__\n"
            text += f"โฑ **Duration:** `{results[i]['duration']}`\n"
            text += f"๐ **View:** `{results[i]['views']}`\n"
            text += f"โ **Channel:** {results[i]['channel']}\n"
            text += f"๐: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.
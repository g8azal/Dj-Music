# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks ยฉ @Dr_Asad_Ali ยฉ Rocks
# Owner Asad + Harshit


from rocksdriver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    MY_BRO,
    REPO_OWNER,
    MY_SERVER,
    BOT_UPDATE,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await message.reply_text(
        f"""<b>๐ฎโ **ูุฑุญุจุง ุจู ุนุฒูุฒู {message.from_user.mention} .** \n
๐งโุงูุง ุจูุช ุชุดุบูู ุงููุฏูู ู ุงูููุณููู ูู ุงูุฏุฑุฏุดุงุช ุงูุตูุชูู.

๐ฅโุงุณุชุทูุน ุงูุถุง ุงูุชุญูู ูู ุงูููุชููุจ ูุฏูู ุงู ุตูุช ุจุฌููุน ุงูุฏูู.

๐ฎโููุนุฑูู ููููู ุชุดุบููู ูู ูุฌููุนุชู ุงุถุบุท ุนูู ุฒุฑ ุงูุงูุฑ ุงูุจูุช ุจุงูุงุณูู ููู ุงุนุฑุถ ูู ุฌููุน ุงูุงูุงูุฑ.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- ุงุถู ุงูุจูุช ููุฌููุนุชู .๏ธ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- ุงูุงูุฑ ุชุดุบูู ุงูุจูุช .", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(
                        "- ุงููุทูุฑ .", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton(
                        "- ุฌุฑูุจ ุงูุฏุนู .", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐๐ ๐8๐ผ๐๐ผ๐ ๐ฆโฝโโโ๐8โ", url="https://t.me/U_Y_H"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฆ- [๐๐ ๐8๐ผ๐๐ผ๐ ๐ฆโฝโโโ๐8โ](https://t.me/G8AZAAL)

โข **ุงุถู @{ASSISTANT_NAME} ูุดุฑู ูู ุฌุฑูุจู ุงู ุงุฑุณู /join ูููุถู ุชููุงุฆู.**

โข **ุงู ูุงุฌูุช ุงู ูุดููู ุฑุงุณููู @G8AZAAL**
ู---------------------------------
โข **ูุฐู ุงูุงูุฑ ุชุดุบูู ุงูุจูุช**
โบ /play (ุงุณู ุงูุงุบููู ุงู ุงููููู) ูุชุดุบูู ุงูุงุบุงูู ู ุงููุญุงุฏุซุงุช
โบ /stream (ุงูุงุณู ุงู ุงูุฑุงุจุท) - ุฏูู ุงูููุณููู ุงูุญูุฉ ุนูู yt ุงูุญูุฉ / ุงูุฑุงุฏูู
โบ /vplay (ุงุณู ุงููุฏูู ุงู ุงููููู) - ูุชุดุบูู ุงููุฏูู ูู ุงููุญุงุฏุซุงุช ุงูุตูุชูู
โบ /vstream - ุชุดุบูู ููุฏูู ูุจุงุดุฑ ูู yt live / m3u8
โบ /playlist - ูุงุธูุงุฑ ูุงุฆูู ุงูุชุดุบูู
โบ /video ุงูุงุณู - ูุชูุฒูู ุงููุฏูู ูู ุงูููุชููุจ
โบ /song ุงูุงุณู - ูุชูุฒูู ุงูุงุบุงูู ูู ุงูููุชููุจ
โบ /search ุงูุงุณู - ููุจุญุซ ุนู ุฑุงุจุท ุงููุฏูู ูู ููุชููุจ
โบ /ping - ุงุธูุงุฑ ุญุงูู ุงูุจูุช
โบ /uptime - ุงุธูุงุฑ ููุช ุชุดุบูู ุงูุจูุช
โบ /alive - ุงุธูุงุฑ ููุช ุชุดุบูู ุงูุจูุช ูู ุงููุฌููุนู

โบ /pause - ุงููุงู ุงูุชุดุบูู ูุคูุชุง
โบ /resume - ุงุณุชุฆูุงู ุงูุชุดุบูู 
โบ /skip - ุชุดุบูู ุงูุงุบููู ุงูุชุงููู
โบ /stop - ุงููุงู ุชุดุบูู ุงูููุณููู
โบ /vmute - ูุชู ุงูุจูุช ูู ุงูุฏุฑุฏุดู ุงูุตูุชูู
โบ /vunmute - ุงูุบุงุก ูุชู ุงูุจูุช ูู ุงูุฏุฑุฏุดู ุงูุตูุชูู
โบ /volume `1-200` - ุถุจุท ูุณุชูู ุงูุตูุช
โบ /reload - ุงุนุงุฏู ุชุญููู ูุชุดุบูู ุงูุจูุช ูู ุงููุฌููุนู
โบ /join - ุงูุถูุงู ุงูุญุณุงุจ ุงููุณุงุนุฏ ุฅูู ูุฌููุนุชู
โบ /userbotleave - ุฎุฑูุฌ ุงูุญุณุงุจ ุงููุณุงุนุฏ ูู ุงููุฌููุนู
โบ /rmw - ุชูุธูู ูุงูุฉ ุงููููุงุช ุงูุฎุงู
โบ /rmd - ุชูุธูู ูุงูุฉ ุงููููุงุช ุงูุชู ุชู ุชูุฒูููุง
โบ /sysinfo - ุฅุธูุงุฑ ูุนูููุงุช ุงููุธุงู

โข **ูุฐู ุงูุงูุงูุฑ ุฎุงุตู ุจุงููุทูุฑ**
โบ /update - ุชุญุฏูุซ ุจูุชู ุงูู ุงุฎุฑ ุงุตุฏุงุฑ
โบ /restart - ุนูู ุฑูุณุชุงุฑุช ููุจูุช
โบ /leaveall - ุฎุฑูุฌ ุงูุจูุช ูู ุฌููุน ุงููุฌููุนุงุช

๐ฆ ุฌููุน ุงูุงูุงูุฑ ุชุฎุต {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ุฑุฌูุน ููุฎูู", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("**สแดแด'สแด แดษด Aษดแดษดสแดแดแดs Aแดแดษชษด !**\n\n**ยป สแดแด?แดสแด สแดแดแด แดแด แดsแดส แดแดแดแดแดษดแด าสแดแด แดแดแดษชษด สษชษขสแดs.**")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก **แดสแดแดขแดส สแดแด แดสแด ษดแดแด แดแดแดษชษด !**", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **sแดแดแดษชษดษขs แดา** {query.message.chat.title}\n\nโธ : **แดแดแดsแด sแดสแดแดแด**\nโถ๏ธ : **สแดsแดแดแด sแดสแดแดแด**\n๐ : **แดแดแดแด แดsแดสสแดแด**n๐ : **แดษดแดแดแดแด แดsแดสสแดแด**\nโน : **แดษดแด sแดสแดแดแด**",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ แดสแดsแด", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ **ษดแดแดสษชษดษข ษชs แดแดสสแดษดแดสส sแดสแดแดแดษชษดษข**", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก **แดสแดแดขแดส สแดแด แดสแด ษดแดแด แดแดแดษชษด !**!", show_alert=True)
    await query.message.delete()
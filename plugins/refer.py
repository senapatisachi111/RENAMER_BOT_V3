from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Share Your Link" ,url=f"https://t.me/share/url?url=https://t.me/MrRenamerRoBot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"☑ 𝐑𝐞𝐟𝐞𝐫 𝐀𝐧𝐝 𝐄𝐚𝐫𝐧 𝐆𝐞𝐭 𝟏𝟎𝟎𝐌𝐁 𝐔𝐩𝐥𝐨𝐚𝐝 𝐋𝐢𝐦𝐢𝐭.\n⚡𝐏𝐞𝐫 𝐑𝐞𝐟𝐞𝐫 𝟏𝟎𝟎𝐌𝐁\n Your Link :- https://t.me/MrRenamerRoBot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    

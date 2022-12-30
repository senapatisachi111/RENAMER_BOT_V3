"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	⚙ Daily  Upload  limit 10GB
	⚙ Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	⚙ Daily Upload limit 50GB
	⚙ Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	
	✪✪ 𝐏𝐚𝐲 𝐮𝐬𝐢𝐧𝐠 𝐔𝐏𝐈 𝐈𝐃 ```mrsns811@kotak```
	
	✪✪ 𝙰𝚏𝚝𝚎𝚛 𝙿𝚊𝚢𝚖𝚎𝚗𝚝 𝚂𝚎𝚗𝚍 \n"𝚂𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝𝚜 𝙾𝚏 𝙿𝚊𝚢𝚖𝚎𝚗𝚝" \n𝚃𝚘 ♚ 𝙰𝙳𝙼𝙸𝙽 ♚."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("♚ 𝙰𝙳𝙼𝙸𝙽 ♚",url = "https://t.me/SNSNS01")], 
        			[InlineKeyboardButton("🌎 𝙿𝙰𝚈𝙿𝙰𝙻 🌎",url = "https://t.me/SNSNS01"),
        			InlineKeyboardButton("🎁 𝙿𝙰𝚈𝚃𝙼 ❤️",url = "https://p.paytm.me/xCTH/e3j2npz7")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	⚙ Daily  Upload  limit 10GB
	⚙ Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	⚙ Daily Upload limit 50GB
	⚙ Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	
	✪✪ 𝐏𝐚𝐲 𝐮𝐬𝐢𝐧𝐠 𝐔𝐏𝐈 𝐈𝐃 ```mrsns811@kotak```
	
	✪✪ 𝙰𝚏𝚝𝚎𝚛 𝙿𝚊𝚢𝚖𝚎𝚗𝚝 𝚂𝚎𝚗𝚍 \n"𝚂𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝𝚜 𝙾𝚏 𝙿𝚊𝚢𝚖𝚎𝚗𝚝" \n𝚃𝚘 ♚ 𝙰𝙳𝙼𝙸𝙽 ♚."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("♚ 𝙰𝙳𝙼𝙸𝙽 ♚",url = "https://t.me/SNSNS01")], 
        			[InlineKeyboardButton("🌎 𝙿𝙰𝚈𝙿𝙰𝙻 🌎",url = "https://t.me/SNSNS01"),
        			InlineKeyboardButton("🎁 𝙿𝙰𝚈𝚃𝙼 ❤️",url = "https://p.paytm.me/xCTH/e3j2npz7")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

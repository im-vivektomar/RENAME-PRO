from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	𝘏𝘦𝘭𝘭𝘰 👋 {message.from_user.first_name }
	
➠ 𝘐'𝘮 𝘈 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘍𝘪𝘭𝘦 🗃️ & 𝘝𝘪𝘥𝘦𝘰 📸 𝘙𝘦𝘯𝘢𝘮𝘦 𝘉𝘰𝘵.

➠ 𝘐 𝘊𝘢𝘯 𝘙𝘦𝘯𝘢𝘮𝘦 ✍️ 𝘈𝘯𝘺 𝘍𝘪𝘭𝘦 🗃️ & 𝘝𝘪𝘥𝘦𝘰 📸 𝘞𝘪𝘵𝘩 𝘊𝘶𝘴𝘵𝘰𝘮 𝘛𝘩𝘶𝘮𝘣𝘯𝘢𝘪𝘭 𝘚𝘶𝘱𝘱𝘰𝘳𝘵.
       
➠ 𝘔𝘢𝘪𝘯𝘵𝘢𝘪𝘯𝘦𝘥 𝘉𝘺 : @ISRAELDESTROYER
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("⚠️ Support" ,url="https://t.me/MIDDLEEASTROYER") ]  ]))


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__𝘞𝘩𝘢𝘵 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘔𝘦 𝘛𝘰 𝘋𝘰 𝘞𝘪𝘵𝘩 𝘛𝘩𝘪𝘴 𝘍𝘪𝘭𝘦?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Rename 📝",callback_data = "rename")
       ,InlineKeyboardButton("Cancel ❌",callback_data = "cancel")  ]]))

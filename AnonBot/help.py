import random
from pyrogram import Client, filters


MESSAGE = ["Just send me direct files I will send you back by removing it's tag. Report bugs at @MysteryBotsChat"]



# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def help(anonbot, msg):
	await msg.reply(MESSAGE)

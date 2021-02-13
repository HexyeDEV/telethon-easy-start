import os, json, asyncio, sys
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient as TMPTelegramClient

API_KEY = "123456789"

API_HASH = "your API_HASH"

bot = TelegramClient("bot2", API_KEY, API_HASH)

@bot.on(events.NewMessage(incoming=True))
async def NewMessages(msg):
    if msg.text == "/start":
       await msg.respond("Hello, I am a bot!",buttons=[[Button.inline("inline keyboard","test")],[Button.url("Link button","https://github.com/condonato/telethon-easy-start/")]])

@bot.on(events.CallbackQuery())
async def callbackQuery(cq):
    if cq.data == b"test1":
       await msg.edit("callback done, message edited!", buttons=[[Button.inline("back","test2")]])
    if cq.data == b"test2":
       await msg.edit("Hello, I am a bot!", buttons=[[Button.inline("inline keyboard","test")],[Button.url("Link button","https://github.com/condonato/telethon-easy-start/")]]) 
       
bot.start()

bot.run_until_disconnected()

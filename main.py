import os, json, asyncio, sys
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient as TMPTelegramClient

API_KEY = "your API_KEY"

API_HASH = "your API_HASH"

bot = TelegramClient("bot2", API_KEY, API_HASH)

@bot.on(events.NewMessage(incoming=True))
async def Start(msg):



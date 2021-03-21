import asyncio
from telethon import TelegramClient, events

api_id = 3517097
api_hash = '4122c2c0e7462dc73e61dc1a88ea3af5'

client  = TelegramClient('session_id', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def my_event_handler(event):
    if '1409209046' in str(event):
        await client.send_message(1158485158, event.raw_text)

client.run_until_disconnected()

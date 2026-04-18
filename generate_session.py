import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 34665549
API_HASH = '9b8c814bdbeddcb2855773c5be6b5492'

async def main():
    print("=" * 50)
    print("  TELETHON SESSION STRING GENERATOR")
    print("=" * 50)
    print()
    
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        await client.start()
        session_string = client.session.save()
        
        print()
        print("=" * 50)
        print("  YOUR SESSION STRING (copy this):")
        print("=" * 50)
        print()
        print(session_string)
        print()
        print("=" * 50)
        print("Paste this as SESSION_STRING in Railway Variables!")
        print("=" * 50)

asyncio.run(main())

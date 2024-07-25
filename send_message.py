import sys
from telethon import TelegramClient
import os

api_id = '20705546'
api_hash = 'a72133f7b59aa863da736995077bdf5c'
phone = '+923093902974'  # Include the country code, e.g., +1234567890
bot_username = '@PayuBiz_clone_Bot'  # Replace with the username of the bot you want to send the message to

# Use a unique session name based on the process ID to avoid conflicts
session_name = f'session_{os.getpid()}'
client = TelegramClient(session_name, api_id, api_hash)

async def main(message):
    await client.start(phone)
    bot = await client.get_entity(bot_username)
    await client.send_message(bot, message)
    print('Message sent')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        message = sys.argv[1]
        with client:
            client.loop.run_until_complete(main(message))
    else:
        print('No message provided')

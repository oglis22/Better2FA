import os
import asyncio
from threading import Thread
from dotenv import load_dotenv
from web.web_server import app
from cogs.bot import bot
from cogs.command_handler import setup_commands
from cogs.event_manager import setup_events
from database import database

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
debug = os.getenv('DEBUG')

setup_events(bot)
setup_commands(bot)

def run_flask():
    app.run(debug=debug, use_reloader=False, threaded=True)

async def run_bot():
    await bot.start(token)

async def main():
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    await run_bot()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

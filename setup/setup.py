import os
from discord import Client
from utils import utils

verify_link_channel_id = os.getenv('VERIFY_LINK_CHANNEL')
discord_auth_link = os.getenv('DISCORD_AUTH_LINK')

async def setup(bot: Client):
    verify_link_channel = bot.get_channel(int(verify_link_channel_id))
    
    if verify_link_channel:
        await verify_link_channel.purge()

    await utils.send_auth_message(verify_link_channel, discord_auth_link)
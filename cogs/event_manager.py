import discord
from cogs.discord_authentication import is_account_suspicious
import os
from utils.utils import log_message
from setup import setup
from log import Logger

def setup_events(bot: discord.Client):
    @bot.event
    async def on_ready():
        print(f'Better2FA is logged in as {bot.user.id}')
        await setup.setup(bot)

    @bot.event
    async def on_member_join(member: discord.Member):
        verify_role = member.guild.get_role(int(os.getenv('VERIFY_ROLE')))
        await member.add_roles(verify_role)
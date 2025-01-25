import discord
from cogs.discord_authentication import is_account_suspicious
import os
from utils.utils import log_message
from setup import setup


qu_role_id = os.getenv('QUARANTINE_ROLE')
log_channel_id = os.getenv('LOG_CHANNEL_ID')

def setup_events(bot: discord.Client):
    @bot.event
    async def on_ready():
        print(f'Better2FA is logged in as {bot.user.id}')
        await setup.setup(bot)

    @bot.event
    async def on_member_join(member: discord.Member):
        verify_role = member.guild.get_role(int(os.getenv('VERIFY_ROLE')))
        await member.add_roles(verify_role)
        if is_account_suspicious(member):
            role = member.guild.get_role(int(qu_role_id))
            await member.add_roles(role)
            log_channel = bot.get_channel(int(log_channel_id))
            await log_message(log_channel,'Log Message' ,f"Suspicious user joined the server and got blocked {member.name}:{member.id}")

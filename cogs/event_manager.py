import discord
from cogs.discord_authentication import is_account_suspicious
import os
from utils.utils import log_message

qu_role_id = os.getenv('QUARANTINE_ROLE')
log_channel_id = os.getenv('LOG_CHANNEL_ID')

def setup_events(bot: discord.Client):
    @bot.event
    async def on_ready():
        print(f'Better2FA is logged in as {bot.user.id}')

    @bot.event
    async def on_member_join(member: discord.Member):
        if is_account_suspicious(member):
            role = discord.utils.get(member.guild.roles, id=qu_role_id)
            await member.add_roles(role)
            log_channel = bot.get_channel(int(log_channel_id))
            await log_message(log_channel, f"Sus user joined the server and got blocked {member.name}:{member.id}")

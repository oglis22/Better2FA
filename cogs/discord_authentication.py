from datetime import datetime
from dotenv import load_dotenv
import os
import discord
from cogs import bot

load_dotenv()

sus_account_days = int(os.getenv("SUSPICIOUSLY_NEW_ACCOUNT_IN_DAYS"))

def is_account_suspicious(user: discord.Member):
    created_at = user.created_at

    now = datetime.utcnow()
    age = now - created_at

    days = age.days
    if days <= sus_account_days:
        return True
    return False

async def authenticate(id: int):
    guild = bot.get_bot().get_guild(os.getenv("GUILD_ID"))
    member = guild.get_member(id)
    verify_role = member.guild.get_role(int(os.getenv('VERIFY_ROLE')))
    await member.remove_roles(verify_role)
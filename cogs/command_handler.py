import discord
from discord.ext import commands
from database import database

async def banip(ctx, user: discord.User):
    tfauser = database.get_user_by_id(user.id)
    database.ban(discord_id=user.id, ip=tfauser.get('ip'))
    pass

def setup_commands(bot: commands.Bot):
    @bot.command()
    async def ban_ip(ctx, user: discord.User):
        await banip(ctx, user)

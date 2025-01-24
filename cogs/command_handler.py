import discord
from discord.ext import commands

async def banip(ctx, user: discord.User):
    # TODO: Handle command interaction
    pass

def setup_commands(bot: commands.Bot):
    @bot.command()
    async def ban_ip(ctx, user: discord.User):
        await banip(ctx, user)

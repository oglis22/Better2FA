from datetime import datetime
from dotenv import load_dotenv
import os
import discord
from cogs import bot
from log import Logger

load_dotenv()


async def authenticate(id: int):
    guild = bot.get_bot().get_guild(os.getenv("GUILD_ID"))
    member = guild.get_member(id)
    verify_role = member.guild.get_role(int(os.getenv('VERIFY_ROLE')))
    Logger.setup_logger().info("Authenticate User with id: " + id)
    await member.remove_roles(verify_role)
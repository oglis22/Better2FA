import discord
from discord.ext import commands

# Bot-Initialisierung
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def get_bot():
    return bot

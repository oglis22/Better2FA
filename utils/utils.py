import discord
import discord
from discord.ui import View, Button

async def log_message(channel: discord.TextChannel, title: str, msg: str):
    embed = discord.Embed(
        title=title,
        description=msg,
        color=discord.Color.green()
    )

    await channel.send(embed=embed)


async def send_auth_message(channel: discord.TextChannel, link: str):
    button = Button(label="Authenticate", url=link, style=discord.ButtonStyle.link)

    view = View()
    view.add_item(button)

    embed = discord.Embed(
        title="Authentication Required",
        description="Click the button below to authenticate.",
        color=discord.Color.blurple()
    )

    await channel.send(embed=embed, view=view)

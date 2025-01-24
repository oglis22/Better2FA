import discord


async def log_message(channel: discord.TextChannel, msg: str):
    embed = discord.Embed(
        title="Log-Nachricht",
        description=msg,
        color=discord.Color.green()
    )

    await channel.send(embed=embed)
import discord
from database import database

bot = discord.Bot()

@bot.slash_command(name="ban_ip", description="Ban a user")
async def ban_ip(interaction: discord.Interaction, user: discord.User):
    try:
        tfauser = database.get_user_by_id(user.id)
        if tfauser:
            database.ban(discord_id=user.id, ip=tfauser.get('ip'))
            await interaction.response.send_message(f"{user.name} wurde erfolgreich gebannt!")
        else:
            await interaction.response.send_message(f"Benutzer {user.name} nicht gefunden.")
    except Exception as e:
        await interaction.response.send_message(f"Fehler beim Bannen des Benutzers: {str(e)}")

def get_bot():
    return bot

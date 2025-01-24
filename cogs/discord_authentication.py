from datetime import datetime
from dotenv import load_dotenv
import os
import discord

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
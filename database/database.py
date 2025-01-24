import sqlite3


conn = sqlite3.connect('./db/bans.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS bans (
discord_id INT PRIMARY KEY,
startdate VARCHAR(255)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
discord_id INT PRIMARY KEY,
ip VARCHAR(255)
);
''')

def register_user(discord_id: int, ip: str):
    pass

def ban(discord_id: int):
    pass
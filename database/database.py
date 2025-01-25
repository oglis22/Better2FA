import sqlite3
from datetime import datetime

conn = sqlite3.connect('./db/bans.db', check_same_thread=False)
cursor = conn.cursor()

def setup():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        discord_id INT PRIMARY KEY,
        ip VARCHAR(255),
        token VARCHAR(255)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bans (
        discord_id INT PRIMARY KEY,
        startdate VARCHAR(255)
    );
    ''')

    conn.commit()


def register_user(discord_id: int, ip: str, token: str):
    cursor.execute('''
    INSERT OR REPLACE INTO user (discord_id, ip, token) 
    VALUES (?, ?, ?);
    ''', (discord_id, ip, token))

    conn.commit()

    print(f"Client with discord {discord_id} was registerd.")


def ban(discord_id: int):
    startdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
    INSERT OR REPLACE INTO bans (discord_id, startdate) 
    VALUES (?, ?);
    ''', (discord_id, startdate))

    conn.commit()

    print(f"Client with Discord-ID {discord_id} was registerd at {startdate}")

def is_banned(discord_id: int):
    cursor.execute('''
    SELECT startdate FROM bans WHERE discord_id = ?;
    ''', (discord_id,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def close():
    conn.close()

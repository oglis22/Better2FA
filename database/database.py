import sqlite3
from datetime import datetime

conn = sqlite3.connect('./db/db.db', check_same_thread=False)
cursor = conn.cursor()

def setup():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        discord_id INT PRIMARY KEY,
        ip VARCHAR(255),
        token VARCHAR(255),
        log_date DATETIME
    );
    ''')

    conn.commit()

def register_user(discord_id: int, ip: str, token: str):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT OR REPLACE INTO user (discord_id, ip, token, log_date) 
    VALUES (?, ?, ?, ?);
    ''', (discord_id, ip, token, current_time))

    conn.commit()

    print(f"Client with Discord-ID {discord_id} was registered at {current_time}.")

def get_user_by_id(discord_id: int):
    cursor.execute('''
    SELECT discord_id, ip, token, log_date FROM user WHERE discord_id = ?;
    ''', (discord_id,))
    result = cursor.fetchone()

    if result:
        return {"discord_id": result[0], "ip": result[1], "token": result[2], "log_date": result[3]}
    else:
        return None

def close():
    conn.close()

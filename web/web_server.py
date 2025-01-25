import os

from flask import Flask, request, render_template, redirect
from oauth2 import oauth_handler
from blacklist import ip2proxy
from utils import whitelist_config
from database import database
from cogs import discord_authentication

app = Flask(__name__, template_folder='templates')

database.setup()

@app.route('/authentication')
def authenticate():
    client_ip = request.remote_addr
    print(f"New Authentication from: {client_ip}")
    data = oauth_handler.exchange_code(request.args.get('code'))
    white_list = whitelist_config.get_whitelist()
    if client_ip in white_list:
        user_data = oauth_handler.get_discord_user_info(data['access_token'], data['token_type'])
        discord_authentication.authenticate(user_data['id'])
        return redirect(os.getenv("INVITE_LINK"))
    elif ip2proxy.check_address(client_ip):
        return render_template('index.html')
    elif database.is_banned_by_ip(client_ip):
        return render_template('index.html')
    else:
        user_data = oauth_handler.get_discord_user_info(data['access_token'], data['token_type'])
        database.register_user(discord_id=user_data['id'], ip=client_ip, token='none')
        discord_authentication.authenticate(user_data['id'])
        return redirect(os.getenv("INVITE_LINK"))

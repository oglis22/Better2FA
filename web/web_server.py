import os

from flask import Flask, request, render_template, redirect, make_response
from oauth2 import oauth_handler
from blacklist import ip2proxy
from utils import whitelist_config
from database import database
from cogs import discord_authentication
from browser_fingerprint import browser_token

app = Flask(__name__, template_folder='templates')

database.setup()

@app.route('/authentication')
def authenticate():
    client_ip = request.remote_addr
    print(f"New Authentication from: {client_ip}")

    data = oauth_handler.exchange_code(request.args.get('code'))
    white_list = whitelist_config.get_whitelist()
    saved_web_token = request.cookies.get('token')
    user_data = oauth_handler.get_discord_user_info(data['access_token'], data['token_type'])

    if client_ip in white_list:
        discord_authentication.authenticate(user_data['id'])
        return redirect(os.getenv("INVITE_LINK"))

    if ip2proxy.check_address(client_ip) or database.is_banned_by_ip(client_ip):
        return render_template('index.html')

    user = database.get_user_by_id(user_data['id'])
    if user:
        if not saved_web_token or user.get('token') != saved_web_token:
            return render_template('index.html')

    web_token = browser_token.generate_token()
    database.register_user(discord_id=user_data['id'], ip=client_ip, token=web_token)
    discord_authentication.authenticate(user_data['id'])

    resp = make_response(redirect(os.getenv("INVITE_LINK")))
    resp.set_cookie('token', web_token, max_age=60*60*24*365*10)

    return resp
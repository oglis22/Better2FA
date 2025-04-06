import os

from flask import Flask, request, render_template, redirect, make_response
from oauth2 import oauth_handler
from database import database
from cogs import discord_authentication
from log import Logger

RESTAPI_AUTH_TOKEN = os.getenv('RESTAPI_AUTH_TOKEN')

app = Flask(__name__, template_folder='templates')

database.setup()

@app.route('/authentication')
def authenticate():
    client_ip = request.remote_addr
    logger = Logger.setup_logger()
    logger.info("New Authentication from: {client_ip}")

    data = oauth_handler.exchange_code(request.args.get('code'))
    white_list = whitelist_config.get_whitelist()
    saved_web_token = request.cookies.get('token')
    user_data = oauth_handler.get_discord_user_info(data['access_token'], data['token_type'])

    web_token = "token"
    database.register_user(discord_id=user_data['id'], ip=client_ip, token=web_token)
    discord_authentication.authenticate(user_data['id'])
    logger.info("Saved new user data ip: " + client_ip + " id: " + user_data['id'])
    resp = make_response(redirect(os.getenv("INVITE_LINK")))
    resp.set_cookie('token', web_token, max_age=60*60*24*365*10)

    return resp

@app.route('/get_ip/<discord_id>')
def get_ip(discord_id):
    logger = Logger.setup_logger()
    logger.info(f"IP lookup request for Discord ID: {discord_id}")

    auth_token = request.headers.get('Authorization')
    if not auth_token == RESTAPI_AUTH_TOKEN:
        logger.warning("Unauthorized access attempt")
        return {"error": "Unauthorized"}, 401

    user_data = database.get_user_by_id(discord_id)
    if user_data:
        return {"discord_id": discord_id, "ip": user_data['ip'], "log_date": user_data['log_date']}
    else:
        return {"error": "User not found"}, 404
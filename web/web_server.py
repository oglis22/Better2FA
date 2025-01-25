from flask import Flask, request, render_template
from oauth2 import oauth_handler
from blacklist import ip2proxy

app = Flask(__name__, template_folder='templates')

@app.route('/authentication')
def authenticate():
    client_ip = request.remote_addr
    data = oauth_handler.exchange_code(request.args.get('code'))
    if ip2proxy.check_address(client_ip):
        return render_template('index.html')
    else:
        return f'Checking your system ...{data}'
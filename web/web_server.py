from flask import Flask, request

app = Flask(__name__)

@app.route('/authentication')
def authenticate():
    client_ip = request.remote_addr
    return f'Checking your system ...'
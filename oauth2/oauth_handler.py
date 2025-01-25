import requests
import os


def exchange_code(code):
  API_ENDPOINT = 'https://discord.com/api/v10'
  CLIENT_ID = os.getenv("CLIENT_ID")
  CLIENT_SECRET = os.getenv("CLIENT_SECRET")
  REDIRECT_URI = os.getenv("REDIRECT_URI")

  print(REDIRECT_URI)
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()
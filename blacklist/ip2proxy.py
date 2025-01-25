import requests


def check_address(ip_address):
    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
    response = requests.get(url)
    ip_list = response.text.splitlines()
    if ip_address in ip_list:
        return True
    else:
        return False

def add_ip_to_whitelist(ip):
    with open("whitelist.txt", "a") as file:
        file.write(ip + "\n")

def get_whitelist():
    try:
        with open("whitelist.txt", "r") as file:
            ips = [ip.strip() for ip in file.readlines()]
        return ips
    except FileNotFoundError:
        return []
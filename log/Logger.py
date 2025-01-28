import logging
from logging.handlers import RotatingFileHandler

def setup_logger(level=logging.INFO, max_bytes=5*1024*1024, backup_count=3):
    loggerS = logging.getLogger("Better2FA")
    loggerS.setLevel(level)

    file_handler = RotatingFileHandler("logs.txt", maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    loggerS.addHandler(file_handler)
    loggerS.addHandler(console_handler)

    return loggerS
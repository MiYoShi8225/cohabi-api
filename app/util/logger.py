# 標準ライブラリー
import logging
from datetime import datetime

def format():
    formatter = '[%(levelname)s] %(asctime)s : %(message)s'
    logging.basicConfig(format=formatter, filename='./logs/{}.log'.format("app"), level=logging.DEBUG)

def printer(msg, error_level):
    print("[{}] {} : {}".format(error_level, str(datetime.now()).split('.')[0], msg))

def error(msg):
    logging.error(msg)
    printer(msg, 'error')

def warning(msg):
    logging.warning(msg)
    printer(msg, 'warning')

def info(msg):
    logging.info(msg)
    printer(msg, 'info')

def debug(msg):
    logging.debug(msg)
    printer(msg, 'debug')

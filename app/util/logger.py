# 標準ライブラリー
import logging
from datetime import datetime

# 自作ライブラリー
from app.util import switcher



env = switcher.enviroment()

def printer(mes, error_level):
    print("[{}:{}] {} : {}".format(error_level, env, str(datetime.now()).split('.')[0], mes))

def error(mes):
    logging.error(mes)
    printer(mes, 'error')

def warning(mes):
    logging.warning(mes)
    printer(mes, 'warning')

def info(mes):
    logging.info(mes)
    printer(mes, 'info')

def debug(mes):
    logging.debug(mes)
    printer(mes, 'debug')

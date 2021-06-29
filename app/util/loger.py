import logging
import switcher
from datetime import datetime

formatter = '%(asctime)s:%(levelname)s: %(message)s'
env = switcher.enviroment()

class Logger:
    def error(mes):
        logging.error(mes)
        print("{}:{}: {}".format(str(datetime.now()).split('.')[0], env, mes))

    def warning(mes):
        logging.warning(mes)
        print("{}:{}: {}".format(str(datetime.now()).split('.')[0], env, mes))
    
    def info(mes):
        logging.info(mes)
        # print("{}:{}: {}".format(str(datetime.now()).split('.')[0], env, mes))
    
    def debug(mes):
        logging.debug(mes)
        print("{}:{}: {}".format(str(datetime.now()).split('.')[0], env, mes))

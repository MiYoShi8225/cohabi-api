import sys
import json
import logging

import uvicorn

env = sys.argv[1]

def enviroment():
    return env

def app_switch():
    if env == "dev":
        uvicorn.run("app.main:app", port=8080, reload=True, access_log=False)

    if env == "stg":
        pass

    if env == "prd":
        # uvicorn.run("app.main:app", port=8000)
        pass
    else:
        print("Please input args of enviroment name")

def db_switch():
    if env == "dev":
        with open('./key/dev/secret.json') as f:
            acskey = json.load(f)
        return acskey

    if env == "stg":
        pass

    if env == "prd":
        pass


def logger(code_name):
    formatter = '%(asctime)s:%(levelname)s: %(message)s'
    if env == "dev":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.DEBUG)

    if env == "stg":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.INFO)

    if env == "prd":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.INFO)

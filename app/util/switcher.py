# 標準ライブラリー
import sys
import json
import logging

# installライブラリー
import uvicorn

# 引数で渡される環境を変数に格納
env = sys.argv[1]

# 環境の名前を返す
def enviroment():
    return env

# appから呼び出される. uvicornの実行方法を決定する
def app_switch():
    # 開発環境
    if env == "dev":
        # リロードを有効化している
        uvicorn.run("app.main:app", port=8080, reload=True, access_log=False)
        
    # ステージング環境
    if env == "stg":
        pass

    # 本番環境
    if env == "prd":
        # uvicorn.run("app.main:app", port=8000)
        pass
    else:
        print("Please input args of enviroment name")
        pass

# dbの接続先を環境によって変更する
def db_switch():
    if env == "dev":
        with open('./key/dev/secret.json') as f:
            acskey = json.load(f)
        return acskey

    if env == "stg":
        pass

    if env == "prd":
        pass

# ログの設定を環境によって変更する
def logger(code_name):
    formatter = '[%(levelname)s] %(asctime)s : %(message)s'
    if env == "dev":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.DEBUG)

    if env == "stg":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.INFO)

    if env == "prd":
        logging.basicConfig(format=formatter, filename='./logs/{}/{}.log'.format(env, code_name), level=logging.INFO)

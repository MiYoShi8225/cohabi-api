# installライブラリー
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# 自作ライブラリー
from app.db import db_session
from app.routes import router
from app.util import logger, switcher, common
switcher.logger(common.FileName(__file__))

# FastAPIをappに宣言
app = FastAPI()

# originに接続元を許可するURLを記載
origins = [
    "https://cohabi.runemosuky.com"
]

# 接続の許可設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # originsから来たやつを許可している
    allow_credentials=True,
    allow_methods=["*"], # リクエストのメソッドは何でも良い
    allow_headers=["*"],
)

# uvicornから起動した際実行
@app.on_event("startup")
async def startup():
    # TODO: エラーハンドリング(コネクションがうまく行かなかったらログ吐いてプロセスを落とす)
    
    logger.info('start db connect.')

    # dbとのconnectionを作成
    db_session.start_conn()
    

# uvicornを終了した際に実行
@app.on_event("shutdown")
async def shutdown():

    logger.info('end db connect.')

    # dbとのconnectionを切断
    db_session.end_conn()

# ↓これに記載することで他のモジュールで記載したAPIRouterのやつが呼び出される
app.include_router(router)

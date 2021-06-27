from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import db_connection
from app.routes import router



app = FastAPI()

origins = [
    "https://cohabi.runemosuky.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # originsから来たやつを許可している
    allow_credentials=True,
    allow_methods=["*"], # リクエストのメソッドは何でも良い
    allow_headers=["*"],
)

# uvicorn起動した際にdbとコネクションを持つ
@app.on_event("startup")
async def startup():
    print('start')

    # TODO: エラーハンドリング(コネクションがうまく行かなかったらログ吐いてプロセスを落とす)
    db_connection.start()
    

# uvicorn終了した際にdbとコネクションを持つ
@app.on_event("shutdown")
async def shutdown():
    print('test end')
    db_connection.end()

# ↓これに記載することで他のモジュールで記載したAPIRouterのやつが呼び出される
app.include_router(router)

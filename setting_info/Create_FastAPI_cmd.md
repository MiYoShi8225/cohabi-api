## install list
```sh
FastAPI用のモジュール
# pip install fastapi

ASGI用のモジュール
# pip install uvicorn

```

## run FastAPI
```sh
ASGI実行(Application Server Gateway Interface)
# uvicorn main:app --reload

ルートディレクトリにmain.pyがない場合
# uvicorn app.main:app --reload
参考URL
https://qiita.com/yoshi0518/items/52914cd1211eff4b93d0

↓本番実施時
# uvicorn app.main:app
```

## MySQLへのCRUDを行うために必要な物
```sh
MySQLへの書き込みを司るモジュール
# pip install mysqlclient


```
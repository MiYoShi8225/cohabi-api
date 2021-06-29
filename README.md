# cohabi-api

## 実行方法
- /ディレクトにあるapp.pyを実行する
  - 引数に環境名であるdev(開発)/stg(ステージング)/prd(本番)を指定する。

## setting info

- fastAPI 公式ドキュメント

  - https://fastapi.tiangolo.com/ja/

- この repository を動作させる上で行った設定や cmd 郡
  - ./setting_info/を確認

## codeing 方法

- init 情報についての参考 URL

  - https://qiita.com/FN_Programming/items/2dcabc93365a62397afe

- python 命名ルールについての参考 URL

  - https://qiita.com/naomi7325/items/4eb1d2a40277361e898b

- 型情報についての参考 URL

  - https://qiita.com/koralle/items/93b094ddb6d3af917702
  - https://kk-river108.hatenablog.com/entry/2019/03/10/163457

- mysql のコネクションについて

  - https://qiita.com/hoto17296/items/fb1b7304128f4c90af69

- mysqlclinet の conect について

  - https://qiita.com/momomo_rimoto/items/9da8b3f76d9542defd9a

- logging
  - https://docs.python.org/ja/3/howto/logging.html
  - https://develop.blue/2020/02/python-use-logging/
  - https://qiita.com/FukuharaYohei/items/92795107032c8c0bfd19

## directory info

- この repository のディレクトリ構成

  ```txt
  app.py *** uvicornの実行を行う
  |- .gitignore
  |- README.md *** gitのreadme
  |- setting_md/
      |- anaconda_command.md *** anacondaで使うコマンドを記載(これは三善用)
      |- Create_FastAPI_cmd.md *** fastAPIで使うコマンドを記載
      |- directory.txt *** directory情報を記載
  |- app/
      |- __init__.py
      |- main.py *** uvicornに実行されるコマンド
      |- routes.py *** @app.get や@app.postなどを記載
      |- service/ *** リクエスト情報の処理
          |- __init__.py
          |- costs.py
          |- todos.py
          |- calendars.py
          |- categories.py
          |- me.py
          |- groups.py
      |- model/
          |- __init__.py
          |- costs.py
          |- todos.py
          |- calendars.py
          |- categories.py
          |- me.py
          |- groups.py
      |- db/
          |- __init__.py
          |- db_session.py *** dbとのsession(接続)を行う
          |- costs.py
          |- todos.py
          |- calendars.py
          |- categories.py
          |- me.py
          |- groups.py
      |- util
          |- logger.py *** loggingのラッパー
          |- switcher.py *** 環境別の実行を制御する
  |- key/ *** key情報を保管(そのためgitignoreに記載して管理)
      |- dev/
          |- secret_info.json *** dbセッション情報などを格納
      |- stg/
      |- prd
  |- logs/
      |- dev/
      |- stg/
      |- prd/
  |- script/ *** script系を格納する
  |- docker/ *** いつか作られるはず・・・(2021/6/27現在なし)
  ```

  - 参考 URL:
    - https://qiita.com/t-iguchi/items/d01b24fed05db43fd0b8#dbpy
    - https://note.com/yusugomori/n/n9f2c0422dfcd
    - https://nmomos.com/tips/2021/01/23/fastapi-docker-1/

##

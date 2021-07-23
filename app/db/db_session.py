# 標準ライブラリー
import json

# installライブラリー
import MySQLdb
from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor

# 自作ライブラリー
from app.util import logger

# グローバル変数になるものの型を宣言
conn: Connection
cur: Cursor


# dbのconnectを作成する
def start_conn(path):
    global conn
    with open(path) as f:
        acskey = json.load(f)

    # dbのアクセス情報を代入
    db_acs = acskey['database']

    logger.info('start db connect.')

    conn = MySQLdb.connect(
        user=db_acs["user"],
        passwd=db_acs["passwd"],
        host=db_acs["host"],
        db=db_acs["db"],
        charset="utf8mb4",
        connect_timeout=5  # connectionにかかる時間は10秒以内に設定
    )
    conn.ping(True)
    logger.debug(conn)


def end_conn():
    # dbのconnectを閉じる
    conn.close()
    logger.debug(conn)
    logger.info('end mysql connection')

# dbのcursorを作成する


def start_cur():
    global cur
    cur = conn.cursor()
    logger.debug(cur)

# dbのcursorを閉じる


def end_cur():
    cur.close()
    logger.debug(cur)

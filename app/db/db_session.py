# installライブラリー
import MySQLdb
from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor

#自作ライブラリー
from app.util import switcher
from app.util import logger, switcher, common
switcher.logger(common.FileName(__file__))

# dbの情報をswitcherから代入
acskey = switcher.db_switch()

# dbのアクセス情報を代入
db_acs = acskey['database']

# 使用するdbのtable名を持ってくる
table_name = acskey['db_tabele_name']["table1"]

# グローバル変数になるものの型を宣言
conn: Connection
cur: Cursor

# dbのconnectを作成する
def start_conn():
    global conn
    print('start mysql connection')
    
    conn = MySQLdb.connect(
        user=db_acs["user"],
        passwd=db_acs["passwd"],
        host=db_acs["host"],
        db=db_acs["db"],
        connect_timeout=10 # connectionにかかる時間は10秒以内に設定
    )
    
    print(conn)

# dbのconnectを閉じる
def end_conn():
    conn.close()
    print(conn)
    print('end mysql connection')

# dbのcursorを作成する
def start_cur():
    global cur
    cur = conn.cursor()
    print(cur)

# dbのcursorを閉じる
def end_cur():
    cur.close()
    print(cur)

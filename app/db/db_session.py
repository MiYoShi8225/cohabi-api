import MySQLdb
from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor

from app.util import switcher

acskey = switcher.db_switch()

db_acs = acskey['database']

table_name = acskey['db_tabele_name']["table1"]

# Conneciton型に宣言
conn: Connection
cur: Cursor


def start_conn():
    global conn
    print('start connection')
    
    conn = MySQLdb.connect(
        user=db_acs["user"],
        passwd=db_acs["passwd"],
        host=db_acs["host"],
        db=db_acs["db"],
        connect_timeout=10
    )
    
    print(conn)

def end_conn():
    conn.close()
    print(conn)

def start_cur():
    global cur
    cur = conn.cursor()
    print(cur)

def end_cur():
    cur.close()
    print(cur)

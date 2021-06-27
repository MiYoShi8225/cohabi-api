import MySQLdb
import json

from MySQLdb.connections import Connection

# Conneciton型に宣言
conn: Connection

def start():
    global conn
    print('start connection')
    
    with open('./key/secret.json') as f:
        acskey = json.load(f)

    db_acs = acskey['database']

    conn = MySQLdb.connect(
        user=db_acs["user"],
        passwd=db_acs["passwd"],
        host=db_acs["host"],
        db=db_acs["db"]
    )

    print(conn)

def end():
    conn.close()
    print(conn)
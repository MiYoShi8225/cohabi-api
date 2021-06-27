from typing import List
from app.model.user import User
from MySQLdb.cursors import Cursor

def get_helloworlds(cur: Cursor) -> List[User]:

    sql = "select id, name from user"
    cur.execute(sql)
    rows = cur.fetchall()
    print('rowsa: {}'.format(rows))

    users:List[User] = []
    for row in rows:
        user = User()
        user.id = row[0]
        user.name = row[1]
        users.append(user)
    
    return users

    
    # db_connection.conn.commit()

def post_helloworlds(cur:Cursor, user: User):
    insert_sql = "insert into user (id, name) VALUES (%s, %s);"
    
    print('{} \n{}'.format(user.id, user.name))

    log1 = cur.execute(insert_sql, (user.id, user.name, ))

    print(log1)

    return True

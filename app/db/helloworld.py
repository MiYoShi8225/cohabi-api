from typing import List
from app.model.user import User
from app.db import db_session

def get_helloworld() -> List[User]:

    sql = "select id, name from {}".format(db_session.table_name)
    db_session.cur.execute(sql)
    rows = db_session.cur.fetchall()
    print('rowsa: {}'.format(rows))

    users:List[User] = []
    for row in rows:
        user = User()
        user.id = row[0]
        user.name = row[1]
        users.append(user)
    
    return users


def create_helloworld(user: User):
    insert_sql = "insert into {} (id, name) VALUES (%s, %s);".format(db_session.table_name)
    
    print('{} \n{}'.format(user.id, user.name))

    log1 = db_session.cur.execute(insert_sql, (user.id, user.name, ))

    print(log1)

    return True

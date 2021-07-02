# 標準ライブラリー
from typing import List

# 自作ライブラリー
from app.util import logger
from app.model.user import User
from app.db import db_session

def get() -> List[User]:
    
    sql = "select id, name from {}".format('user')
    logger.debug('SQL: {}'.format(sql))
    db_session.cur.execute(sql)

    rows = db_session.cur.fetchall()
    
    logger.debug('result: {}'.format(rows))

    users:List[User] = []
    for row in rows:
        user = User()
        user.id = row[0]
        user.name = row[1]
        users.append(user)
    
    return users


def create(user: User):
    sql = "insert into {} (id, name) VALUES (%s, %s);".format('user')
    logger.debug('SQL: {}'.format(sql))
    logger.debug('{} \n{}'.format(user.id, user.name))

    result = db_session.cur.execute(sql, (user.id, user.name, ))

    logger.debug(result)

    return True

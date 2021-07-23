# 標準ライブラリー
from typing import List

# 自作ライブラリー
from app.util import logger
from app.model.user import User
from app.db import db_session

def get(user_id) -> List[User]:
    
    sql = "select * from user where id='{}'".format(user_id)
    logger.debug('SQL: {}'.format(sql))
    db_session.cur.execute(sql)

    rows = db_session.cur.fetchall()
    
    logger.debug('result: {}'.format(rows))

    user = User()
    user.id = rows[0][0]
    user.name = rows[0][1]
    user.mail = rows[0][3]
    
    return user

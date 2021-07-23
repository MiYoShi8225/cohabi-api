# 標準ライブラリー
from typing import List
from app.model import group

# 自作ライブラリー
from app.util import logger
from app.model.group import Group
from app.db import db_session

def get(group_id) -> Group:
    
    sql = "select * from `group` where id='{}'".format(group_id)
    logger.debug('SQL: {}'.format(sql))
    db_session.cur.execute(sql)

    rows = db_session.cur.fetchall()
    
    logger.debug('result: {}'.format(rows))

    group = Group()
    group.id = rows[0][0]
    group.name = rows[0][1]

    return group

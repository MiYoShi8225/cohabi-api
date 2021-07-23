# 標準ライブラリー
from typing import List

# 自作ライブラリー
from app.util import logger
from app.model.membership import Membership
from app.db import db_session

def get(user_id) -> List[Membership]:
    
    sql = "select * from `membership` where user_id='{}'".format(user_id)
    logger.debug('SQL: {}'.format(sql))
    db_session.cur.execute(sql)

    rows = db_session.cur.fetchall()
    
    logger.debug('result: {}'.format(rows))
    
    memberships:List[Membership] = []
    for group_info in rows:
        membership = Membership()
        membership.user_id = group_info[1]
        membership.group_id = group_info[0]
        memberships.append(membership)

    return memberships

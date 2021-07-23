# 自作ライブラリー
from app.util import logger
from app.model.user import User
from app.db import db_session, user as user_session, membership as membership_session, group as group_session


def get(user_id):
    db_session.start_cur()
    user_info = user_session.get(user_id)
    logger.debug('rows: {}'.format(user_info))
    db_session.end_cur()

    db_session.start_cur()
    membership_info = membership_session.get(user_id)
    logger.debug('rows: {}'.format(membership_info))
    db_session.end_cur()

    for membership in membership_info:
        db_session.start_cur()
        group_info = group_session.get(membership.group_id)
        logger.debug('rows: {}'.format(group_info))
        db_session.end_cur()

    retrun_info = [user_info, ]

    return retrun_info

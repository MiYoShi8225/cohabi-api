# 自作ライブラリー
from app.util import logger
from app.model.user import User
from app.db import db_session, helloworld as helloworld_repository


def get():
    db_session.start_cur()
    users = helloworld_repository.get()
    logger.debug('rows: {}'.format(users))

    user_names = []
    for user in users:
        user_names.append(user.name)

    db_session.end_cur()

    return user_names

def create(name):
    from uuid import uuid4
    db_session.start_cur()
    logger.debug('item: {}'.format(name))
    id_code = uuid4()

    user = User()

    user.id = id_code
    user.name = name

    helloworld_repository.create(user)
    
    db_session.conn.commit()
    db_session.end_cur()

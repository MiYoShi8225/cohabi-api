from app.model.user import User
from app.db import db_session, helloworld


def get_helloworld():
    db_session.start_cur()
    users = helloworld.get_helloworld()
    print('rows: {}'.format(users))

    user_names = []
    for user in users:
        user_names.append(user.name)

    db_session.end_cur()

    return user_names

def create_helloworld(name):
    from uuid import uuid4
    db_session.start_cur()
    print('item: {}'.format(name))
    id_code = uuid4()

    user = User()

    user.id = id_code
    user.name = name

    helloworld.create_helloworld(user)

    db_session.end_cur()
    db_session.conn.commit()

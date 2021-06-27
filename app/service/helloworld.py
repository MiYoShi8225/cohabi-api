from app.model.user import User
from app.db import db_connection, helloworld


def get_helloworlds():
    cur = db_connection.conn.cursor()
    users = helloworld.get_helloworlds(cur)
    print('rows: {}'.format(users))

    user_names = []
    for user in users:
        user_names.append(user.name)

    cur.close()

    return user_names

    
    # db_connection.conn.commit()

def post_helloworld(name):
    from uuid import uuid4
    cur = db_connection.conn.cursor()
    print('item: {}'.format(name))
    id_code = uuid4()

    user = User()

    user.id = id_code
    user.name = name

    helloworld.post_helloworlds(cur, user)

    cur.close()
    db_connection.conn.commit()

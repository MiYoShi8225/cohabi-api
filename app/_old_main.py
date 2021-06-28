from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import MySQLdb
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
import json

with open('./key/secret.json') as f:
    acskey = json.load(f)

db_acs = acskey['database']
print(db_acs)

# conn = MySQLdb.connect(
#     user=db_acs["user"],
#     passwd=db_acs["passwd"],
#     host=db_acs["host"],
#     db=db_acs["db"])

app = FastAPI()

origins = [
    "https://cohabi.runemosuky.com"
]

"""
allow_origins=origins,
  originalから来たやつを許可している

allow_credentials=True,
  

allow_methods=["*"],
  リクエストのメソッドは何でも良い
  optionsは必ず入れなきゃいけない(ただしこのケースに限る)
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def get_helloworld():
    print("test")
    mes = {"mes": "helloworld"}
    return mes

@app.get("/helloworld")
def read_root():

    cur = conn.cursor()
    sql = "select id, name from user"
    cur.execute(sql)
    rows = cur.fetchall()
    print('rows: {}'.format(rows))

    user_names = []
    for row in rows:
        user_names.append(row[1])

    result = {
        "error_code": "",
        "error_messages": []
    }

    body = {
        'users': user_names
    }

    return_body = {
        'result': result,
        'body': body
    }

    cur.close()
    conn.commit()
    return return_body


class Item2(BaseModel):
    name: str


@app.post("/helloworld")
def post_root(body: Item2):

    cur = conn.cursor()
    print('item: {}'.format(body))

    insert_sql = "insert into user (id, name) VALUES (%s, %s);"
    id_code = uuid4()

    print('{} \n{}'.format(id_code, body.name))

    log1 = cur.execute(insert_sql, (id_code, body.name, ))

    print(log1)

    cur.close()
    conn.commit()


    result = {
        "error_code": "",
        "error_messages": []
    }

    body = {
        'users': ""
    }

    return_body = {
        'result': result,
        'body': ""
    }

    return return_body


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

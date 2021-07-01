# installライブラリー
from fastapi import APIRouter
from app.service import helloworld
from pydantic import BaseModel

router = APIRouter()

# returnする際のクラスを作成
class ReturnType:
    def __init__(self, body:dict):
        self.result = {
            "error_code": "",
            "error_messages": []
        }

        self.body = body

        self.return_body = {
            'result': self.result,
            'body': self.body
        }


@router.get("/helloworld")
async def get_helloworld():
    user_names = helloworld.get_helloworld()
    
    body = {
        'users': user_names
    }

    return_type = ReturnType(body)

    print(return_type.return_body)
    return return_type.return_body

# input情報の入力値を決定する
class postUser(BaseModel):
    name: str

@router.post("/helloworld")
async def create_helloworld(body: postUser):
    helloworld.create_helloworld(body.name)

    body = {
        'users': ""
    }
    return_type = ReturnType(body)

    print(return_type.return_body)
    return return_type.return_body

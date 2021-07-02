# installライブラリー
from app.util import logger
from fastapi import APIRouter
from app.service import helloworld as helloworld_service
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


@router.get("/helloworld")
async def get_helloworld():
    user_names = helloworld_service.get()
    
    body = {
        'users': user_names
    }

    return_type = ReturnType(body)

    logger.debug(return_type)
    return return_type

# input情報の入力値を決定する
class postUser(BaseModel):
    name: str

@router.post("/helloworld")
async def create_helloworld(body: postUser):
    helloworld_service.create(body.name)

    # TODO: クリエイトしたユーザーを返す
    body = {
        'users': ""
    }
    result = ReturnType(body)

    logger.debug(result)
    return result

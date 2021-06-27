from fastapi import APIRouter
from app.service import helloworld
from pydantic import BaseModel

router = APIRouter()

@router.get("/helloworld")
async def get_helloworld():
    user_names = helloworld.get_helloworlds()

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

    return return_body

class postUser(BaseModel):
    name: str

@router.post("/helloworld")
async def post_helloworld(body: postUser):
    helloworld.post_helloworld(body.name)

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

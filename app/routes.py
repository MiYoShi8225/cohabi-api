# installライブラリー
from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel

from app.auth.authorizer import authorized_user, AuthResult
from app.service import helloworld as helloworld_service, user as user_service
from app.model.api_result import ApiError, ApiResult
from app.util import logger

router = APIRouter()


@router.get("/helloworld")
async def get_helloworld(auth: AuthResult = Depends(authorized_user)):
    # TODO: 毎回これを書くのが面倒なのでAuth Filter的な実装にしたい
    if auth.user == None:
        return ApiResult(result=ApiError(error_code=auth.error_code, error_messages=[auth.error_detail]))

    user_names = helloworld_service.get()

    body = {
        'users': user_names
    }

    result = ApiResult(body=body)

    logger.debug(result.to_json())
    return result


# input情報の入力値を決定する
class postUser(BaseModel):
    name: str


@router.post("/helloworld")
async def create_helloworld(body: postUser, auth: AuthResult = Depends(authorized_user)):
    if auth.user == None:
        return ApiResult(result=ApiError(error_code=auth.error_code, error_messages=[auth.error_detail]))

    helloworld_service.create(body.name)

    # TODO: クリエイトしたユーザーを返す
    body = {
        'users': ""
    }
    result = ApiResult(body=body)

    logger.debug(result.to_json())
    return result

# ↓cohabiコード

@router.get("/users/{user_id}")
async def get_user_info(user_id, auth: AuthResult = Depends(authorized_user)):
    if auth.user == None:
        return ApiResult(result=ApiError(error_code=auth.error_code, error_messages=[auth.error_detail]))
    
    user = user_service.get(user_id)

    body = {
        'name': user.name,
        'id': user.id,
        'mail': user.mail
    }

    result = ApiResult(body=body)

    logger.debug(result.to_json())
    return result

@router.get("/{group_id}/home")
async def get_group_info(group_id, auth: AuthResult = Depends(authorized_user)):
    if auth.user == None:
        return ApiResult(result=ApiError(error_code=auth.error_code, error_messages=[auth.error_detail]))
        
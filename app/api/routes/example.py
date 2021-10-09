from app.schemas.users import UserInfo
from fastapi import APIRouter
from starlette.status import HTTP_400_BAD_REQUEST

router = APIRouter()


@router.get("/info", response_model=UserInfo, name="users:get-user-info")
async def get_user_info() -> UserInfo:
    pass


@router.get("/")
async def hello():
    return {"text": "hello example"}

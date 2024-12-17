from fastapi import APIRouter, Depends

from utils.auth_token import validate_token

check_router = APIRouter()


@check_router.post("/check")
async def _(token_payload: dict = Depends(validate_token)):
    user_id = token_payload.get("user_id")
    nickname = token_payload.get("nickname")

    return {
        "status": 0,
        "message": "OK",
        "userID": user_id,
        "username": nickname
    }

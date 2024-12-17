import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from crud.UserCrud import UserCrud
from schema.User.UserAuthSchema import UserAuthSchema
from utils.auth_token import create_token
from utils.get_db import get_db
from utils.hash_string import hash_string

auth_router = APIRouter()


@auth_router.post("/auth")
async def _(body: UserAuthSchema, db: Session = Depends(get_db)):
    email = body.email
    password = body.password
 
    try:
        user = UserCrud.get_by_email(db, email)
        
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"DataBase Error: {e}"})

    hashed_password = hash_string(password)

    if user is None or user.password != hashed_password:
        return JSONResponse(status_code=401, content={"status": 1, "message": f"Wrong email or password"})

    token = None

    payload = {
        "user_id": user.id,
        "email": user.email,
        "nickname": user.nickname
    }

    token = create_token(payload)


    return {
        "status": 0,
        "message": "OK",
        "token": token,
        "userID": user.id,
        "nickname": user.nickname,
        "email": user.email,
    }

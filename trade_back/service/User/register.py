import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import config
from crud.UserCrud import UserCrud
from schema.User.UserRegisterSchema import UserRegisterSchema
from utils.get_db import get_db
from utils.hash_string import hash_string

register_router = APIRouter()


@register_router.post("/register")
async def _(body: UserRegisterSchema, db: Session = Depends(get_db)):
    password = body.password
    nickname = body.nickname
    email = body.email

    if len(email) > config.user_email_max:
        return JSONResponse(status_code=400, content={"status": 1, "message": "Email too long"})

    if not (config.user_name_min <= len(nickname) <= config.user_name_max):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Username length invalid"})

    if not (config.user_password_min <= len(password) <= config.user_password_max):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Password length invalid"})
    
    try:
        user = UserCrud.get_by_email(db, email)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database error: {e}"})
    
    if user:
            return JSONResponse(status_code=400, content={"status": 1, "message": "Email already exists"})  
       
    user = UserCrud.create(db, nickname, hash_string(password), email)
            
    return {
        "status": 0,
        "message": "OK",
        "email": user.email,
        "userID": user.id,
        "nickname": user.nickname,
    }

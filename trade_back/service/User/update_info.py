import traceback
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import config
from crud.UserCrud import UserCrud
from schema.User.UserUpdateInfoSchema import UserUpdateInfoSchema
from utils.auth_token import validate_token
from utils.get_db import get_db
from utils.hash_string import hash_string
from model.UserModel import User

update_info_router = APIRouter()

@update_info_router.put("/updateInfo")
async def _(body: UserUpdateInfoSchema, token_payload: dict = Depends(validate_token), db: Session = Depends(get_db)):
    user_id = token_payload.get("user_id")
    email = body.email
    password = body.password
    nickname = body.nickname
    gender = body.gender
    age = body.age
    contact = body.contact
    reputation = body.reputation

    if nickname != "" and not (config.user_name_min <= len(nickname) <= config.user_name_max):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Username length invalid"})

    if password != "" and not (config.user_password_min <= len(password) <= config.user_password_max):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Password length invalid"})
    
    if gender != "" and not (gender in ['male', 'female', 'other']):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Gender invalid"})
    

    try:
        user = UserCrud.get_by_id(db, User, user_id)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    if user is None:
        return JSONResponse(status_code=404, content={"status": 1, "message": "User Not Found"})

    try:
        if email != "": user.email = email     
        if password != "": user.password = hash_string(password)
        if nickname != "": user.nickname = nickname
        if gender != "": user.gender = gender
        if age != "": user.age = age
        if contact != "": user.contact = contact
        if reputation != "": user.reputation = reputation
        
        UserCrud.update(db, User, user)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    return {
        "status": 0,
        "message": "OK"
    }

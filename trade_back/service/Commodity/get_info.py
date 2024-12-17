import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from crud.CommodityCrud import CommodityCrud
from utils.auth_token import validate_token
from utils.get_db import get_db
from model.CommodityModel import Commodity

get_info_router = APIRouter()

@get_info_router.get("/getInfo")
async def _(id: int , token_payload: dict = Depends(validate_token), db: Session = Depends(get_db)):
    user_id = token_payload.get("user_id")
    
    try:
        commodity = CommodityCrud.get_by_id(db, Commodity, id)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    if commodity is None:
        return JSONResponse(status_code=404, content={"status": 1, "message": "Commodity Not Found"})

    return {
        "status": 0,
        "message": "OK",
        "data": {
            "user_id": commodity.user_id,
            "name": commodity.name,
            "description": commodity.description,
            "price": commodity.price,
            "category": commodity.category,
            "status": commodity.status,
            "image": commodity.image
        }
    }
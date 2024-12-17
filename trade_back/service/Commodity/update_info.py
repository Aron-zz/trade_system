import traceback
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import config
from crud.CommodityCrud import CommodityCrud
from schema.Commodity.CommodityUpdateInfoSchema import CommodityUpdateInfoSchema
from utils.auth_token import validate_token
from utils.get_db import get_db
from model.CommodityModel import Commodity

update_info_router = APIRouter()

@update_info_router.put("/updateInfo")
async def _(body: CommodityUpdateInfoSchema, token_payload: dict = Depends(validate_token), db: Session = Depends(get_db)):
    user_id = body.user_id
    id = body.id
    name = body.name
    description = body.description
    price = body.price
    category = body.category
    status = body.status
    image = body.image

    if name != "" and not (config.commodity_name_min <= len(name) <= config.commodity_name_max):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Commodity_name length invalid"})

    if price != "" and not (price < 0):
        return JSONResponse(status_code=400, content={"status": 1, "message": "Price invalid"})
    
    try:
        commodity = CommodityCrud.get_by_id(db, Commodity, id)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    if commodity is None:
        return JSONResponse(status_code=404, content={"status": 1, "message": "Commodity Not Found"})

    try:     
        if name != "": commodity.name = name
        if description != "": commodity.description = description
        if price != "": commodity.price = price
        if category != "": commodity.category = category
        if status != "": commodity.status = status
        if image != "": commodity.image = image
        
        CommodityCrud.update(db, Commodity, commodity)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    return {
        "status": 0,
        "message": "OK"
    }

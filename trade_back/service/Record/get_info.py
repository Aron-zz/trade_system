import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from crud.RecordCrud import RecordCrud
from utils.auth_token import validate_token
from utils.get_db import get_db
from model.RecordModel import Record

get_info_router = APIRouter()

@get_info_router.get("/getInfo")
async def _(id:int , token_payload: dict = Depends(validate_token), db: Session = Depends(get_db)):

    try:
        record = RecordCrud.get_by_id(db, Record, id)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    if Record is None:
        return JSONResponse(status_code=404, content={"status": 1, "message": "Record Not Found"})

    return {
        "status": 0,
        "message": "OK",
        "data": {
            "buyer_id": record.buyer_id,
            "seller_id": record.seller_id,
            "commodity_id": record.commodity_id,
            "quantity": record.quantity,
            "total": record.total,
            "status": record.status
        }
    }
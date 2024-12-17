import traceback
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import config
from crud.RecordCrud import RecordCrud
from schema.Record.RecordUpdateInfoSchema import RecordUpdateInfoSchema
from utils.auth_token import validate_token
from utils.get_db import get_db
from model.RecordModel import Record

update_info_router = APIRouter()

@update_info_router.put("/updateInfo")
async def _(body: RecordUpdateInfoSchema, token_payload: dict = Depends(validate_token), db: Session = Depends(get_db)):
    id = body.id
    buyer_id = body.buyer_id
    seller_id = body.seller_id
    commodity_id = body.commodity_id
    quantity = body.quantity
    total = body.total
    status = body.status

    try:
        record = RecordCrud.get_by_id(db, Record, id)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    if record is None:
        return JSONResponse(status_code=404, content={"status": 1, "message": "Record Not Found"})

    try:     
        if buyer_id != "": record.buyer_id = buyer_id
        if commodity_id != "": record.commodity_id = commodity_id
        if quantity != "": record.quantity = quantity
        if total != "": record.total = total
        if status != "": record.status = status
        
        RecordCrud.update(db, Record, record)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": 1, "message": f"Database Error: {e}"})

    return {
        "status": 0,
        "message": "OK"
    }

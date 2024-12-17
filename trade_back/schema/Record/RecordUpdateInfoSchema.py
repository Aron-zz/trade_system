from pydantic import BaseModel

class RecordUpdateInfoSchema(BaseModel):
    id: int
    buyer_id: int
    seller_id: int
    commodity_id: int
    quantity: int
    total: float
    status: str

from pydantic import BaseModel

class CommodityUpdateInfoSchema(BaseModel):
    id: int
    user_id: int
    name: str
    description: str
    price: float
    category: str
    status: str
    image: str 

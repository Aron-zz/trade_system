from pydantic import BaseModel

class UserRegisterSchema(BaseModel):
    nickname: str
    password: str
    email: str

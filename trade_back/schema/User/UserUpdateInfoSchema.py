from pydantic import BaseModel

class UserUpdateInfoSchema(BaseModel):
    email: str       # 邮箱
    password: str   #密码
    nickname: str   # 昵称
    gender: str    # 性别
    age: int    # 年龄
    contact: str    # 联系方式
    reputation: int # 信誉积分

from sqlalchemy import Column, Integer, String, CHAR, Enum, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 用户id，主键，自增
    email = Column(String(100), unique=True, nullable=False)  # 邮箱，最长100字符，唯一，非空
    password = Column(String(255), nullable=False)  # 密码，最长255字符，非空
    nickname = Column(String(50),nullable=False) #昵称，最长50字符，非空
    gender = Column(Enum("male", "female", "other", name="gender_enum"), nullable=False)  # 性别，枚举类型，非空
    age = Column(Integer, nullable=True)  # 年龄，可为空
    contact = Column(String(100), nullable=True)  #联系方式
    reputation = Column(Integer,nullable=True)  # 信誉积分
    created = Column(TIMESTAMP, nullable=False, server_default=func.now())  # 创建时间，默认为当前时间
    
    def __init__(self, email, password, nickname, gender, age=None, contact=None, reputation=None, created=None):
        
        self.email = email
        self.password = password
        self.nickname = nickname
        self.gender = gender
        self.age = age
        self.contact = contact
        self.reputation = reputation
        self.created = created

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, nickname={self.nickname}, gender={self.gender}, age={self.age}, contact={self.contact}, reputation={self.reputation}, created={self.created})>"

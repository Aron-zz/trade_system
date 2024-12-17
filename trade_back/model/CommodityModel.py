from sqlalchemy import Column, Integer, String, Text, DECIMAL, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Commodity(Base):
    __tablename__ = "commodity"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 商品ID
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # 发布商品的用户ID，外键关联用户表
    name = Column(String(100), nullable=False)  # 商品名称
    description = Column(Text)  # 商品描述
    price = Column(DECIMAL(10, 2), nullable=False)  # 商品价格
    category = Column(String(50))  # 商品分类
    status = Column(Enum('available', 'sold', 'removed', name='commodity_status'), default='available')  # 商品状态
    image = Column(String(255))  # 商品图片链接
    created = Column(TIMESTAMP, default=func.now())  # 商品创建时间
    updated = Column(TIMESTAMP, default=func.now(), onupdate=func.now())  # 商品更新时间

    # 定义与User表的关系
    user = relationship("User", backref="commodities")

    def __init__(self, user_id, name, price, description=None, category=None, status='available', image=None, created=None, updated=None):
        self.user_id = user_id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.status = status
        self.image = image
        self.created = created
        self.updated = updated

    def __repr__(self):
        return f"<Commodity(id={self.id}, name={self.name}, price={self.price}, status={self.status})>"

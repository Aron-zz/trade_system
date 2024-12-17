from sqlalchemy import Column, Integer, ForeignKey,  Enum, TIMESTAMP, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 交易记录ID
    buyer_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # 买家ID，外键关联到User表
    seller_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # 卖家ID，外键关联到User表
    commodity_id = Column(Integer, ForeignKey('commodity.id'), nullable=False)  # 商品ID，外键关联到Commodity表
    quantity = Column(Integer, nullable=False)  # 购买数量
    total = Column(DECIMAL(10, 2), nullable=False)  # 交易总价
    status = Column(Enum('pending', 'accepted', 'completed', 'canceled', name='record_status'), default='pending')  # 交易状态
    created = Column(TIMESTAMP, default=func.now())  # 交易创建时间
    updated = Column(TIMESTAMP, default=func.now(), onupdate=func.now())  # 交易更新时间

    # 定义与User表和Commodity表的关系
    buyer = relationship("User", foreign_keys=[buyer_id], backref="purchases")
    seller = relationship("User", foreign_keys=[seller_id], backref="sales")
    commodity = relationship("Commodity", backref="records")

    def __init__(self, buyer_id, seller_id, commodity_id, quantity, total, status='pending', created=None, updated=None):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.commodity_id = commodity_id
        self.quantity = quantity
        self.total = total
        self.status = status
        self.created = created
        self.updated = updated

    def __repr__(self):
        return f"<Record(id={self.id}, buyer_id={self.buyer_id}, seller_id={self.seller_id}, total={self.total}, status={self.status})>"

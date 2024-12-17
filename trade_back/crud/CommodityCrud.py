from sqlalchemy.exc import IntegrityError
from typing import Union
from sqlalchemy.orm import Session
from model.CommodityModel import Commodity
from .Crud import AbstractCrud
from decimal import Decimal

class CommodityCrud(AbstractCrud[Commodity]):
    @staticmethod
    def create(
        db: Session,
        user_id: int,
        name: str,
        description: str = None,
        price: float = 0.0,
        category: str = None,
        status: str = 'available',
        image: str = None
    ) -> Commodity:
        """
        创建一条新的商品记录
        """
        try:
            new_commodity = Commodity(
                user_id=user_id,
                name=name,
                description=description,
                price=price,
                category=category,
                status=status,
                image=image
            )
            db.add(new_commodity)
            db.commit()
            db.refresh(new_commodity)
            return new_commodity
        except IntegrityError as e:
            db.rollback()  # 回滚事务
            print(f"Error: {e.orig}")
            return None

    @staticmethod
    def update_status(db: Session, commodity_id: int, status: str) -> Union[Commodity, None]:
        """
        更新商品的状态（如 'available', 'sold', 'removed'）
        """
        commodity = AbstractCrud.get_by_id(db, Commodity, commodity_id)
        if commodity:
            commodity.status = status
            db.commit()
            db.refresh(commodity)
            return commodity
        return None


from sqlalchemy.exc import IntegrityError
from typing import Union
from sqlalchemy.orm import Session
from model.RecordModel import Record
from .Crud import AbstractCrud

class RecordCrud(AbstractCrud[Record]):
    @staticmethod
    def create(
        db: Session,
        buyer_id: int,
        seller_id: int,
        commodity_id: int,
        quantity: int,
        total: float,
        status: str = 'pending'
    ) -> Record:
        """
        创建一条新的交易记录
        """
        try:
            new_record = Record(
                buyer_id=buyer_id,
                seller_id=seller_id,
                commodity_id=commodity_id,
                quantity=quantity,
                total=total,
                status=status
            )
            db.add(new_record)
            db.commit()
            db.refresh(new_record)
            return new_record
        except IntegrityError as e:
            db.rollback()  # 回滚事务
            print(f"Error: {e.orig}")
            return None

    @staticmethod
    def update_status(db: Session, record_id: int, status: str) -> Union[Record, None]:
        """
        更新交易记录的状态（如 'pending', 'accepted', 'completed', 'canceled'）
        """
        record = AbstractCrud.get_by_id(db, Record, record_id)
        if record:
            record.status = status
            db.commit()
            db.refresh(record)
            return record
        return None

    

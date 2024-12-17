from sqlalchemy.orm import Session
from typing import Union
from model.UserModel import User
from .Crud import AbstractCrud

class UserCrud(AbstractCrud[User]):
    @staticmethod
    def create(
        db: Session, 
        email: str,
        password: str, 
        nickname: str,
        gender: str = "other",
        age: int = None, 
        contact: str = None, 
        reputation: str = None, 
        created: str = None
    ) -> User:
        """
        创建一个新的用户记录
        """
        new_user = User(
            email=email,
            password=password, 
            nickname=nickname, 
            gender=gender, 
            age=age, 
            contact=contact, 
            reputation=reputation, 
            created=created
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    
    
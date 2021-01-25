from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'seller'
    __name = Column('name', String(length=100) )
    __phone = Column('phone', String(length=18) )
    __email = Column('email', String(length=30) )

    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email(self) -> str:
        return self.__email

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @phone.setter
    def phone(self, phone: str) -> None:
        self.__phone = phone
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

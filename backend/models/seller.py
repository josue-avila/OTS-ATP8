from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'
    __name = Column('fullname', String(length=100) )
    __phone = Column( String(length=20) )
    __email = Column( String(length=100) )

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

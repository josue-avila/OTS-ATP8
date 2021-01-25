from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'seller'
    name = Column('name', String(length=100) )
    phone = Column('phone', String(length=18) )
    email = Column('email', String(length=30) )

    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.name = name
        self.phone = phone
        self.email = email

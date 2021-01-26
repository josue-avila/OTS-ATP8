import re

from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    name = Column('name', String(length=100) )
    phone = Column('phone', String(length=18) )
    email = Column('email', String(length=30) )

    @validates('email')
    def validate_email(self, key, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        raise ValueError('Invalid email!')

    @validates('phone')
    def validate_phone(self, key, phone):
        if not re.search('[a-zA-Z]', phone):
            return phone
        raise ValueError("Phone can't have a character")

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

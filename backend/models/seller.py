import re

from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    name = Column('name', String(length=100))
    phone = Column('phone', String(length=18))
    email = Column('email', String(length=30))

    @validates('email')
    def validate_email(self, key, email):
        if email is None:
            raise ValueError("Please write a email number!")
        elif email.strip(' ') == '':
            raise ValueError("Email can't be null!")
        elif re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        raise ValueError('Invalid email!')

    @validates('phone')
    def validate_phone(self, key, phone):
        if phone is None:
            raise ValueError("Please write a phone number!")
        elif phone.strip(' ') == '':
            raise ValueError("Phone can't be null!")
        elif re.search('[a-zA-Z]', phone):
            raise ValueError("Phone can't have a character!")
        return phone

    @validates('name')
    def validate_name(self, key, name):
        if name is None:
            raise ValueError("Please write a name number!")
        elif name.strip(' ') == '':
            raise ValueError("Name can't be null!")
        elif name.strip(' ') != '':
            return name
        raise ValueError("Name can't be null!")

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

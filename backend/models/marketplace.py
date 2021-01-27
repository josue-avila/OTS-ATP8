import re

from backend.models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import validates


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=300), nullable=True)


    @validates('name')
    def validate_name(self, key, name):
        if name is None:
            raise ValueError("Please write a name number!")
        elif name.strip(' ') == '':
            raise ValueError("Name can't be null!")
        return name
    
    @validates('description')
    def validate_name(self, key, description):
        if len(description) > 300:
            raise ValueError("Please, a description has exceeded the 300 character limit!")
        return description


    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

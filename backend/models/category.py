from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(length=150))
    description = Column(String(length=200))

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description

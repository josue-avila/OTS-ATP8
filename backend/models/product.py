from sqlalchemy import Column, String, Numeric

from backend.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=200), nullable=True)
    price = Column(Numeric, nullable=False)

    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

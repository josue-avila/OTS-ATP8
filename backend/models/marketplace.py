from backend.models.base_model import BaseModel
from sqlalchemy import String, Column


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=300), nullable=True)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

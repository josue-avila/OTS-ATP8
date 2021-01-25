from _datetime import datetime
from backend.models.base_model import BaseModel
from sqlalchemy import Column, DATETIME, String


class Log(BaseModel):
    __tablename__ = 'log'
    timestamp = Column(String(length=20), nullable=False)
    operation = Column(String(length=20), nullable=False)
    description = Column(String(length=300), nullable=False)

    def __init__(self, operation: str, description: str):
        date = datetime.now()
        date_formated = date.strftime("%d/%m/%Y %H:%M:%S")
        self.timestamp = date_formated
        self.operation = operation
        self.description = description
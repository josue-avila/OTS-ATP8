from _datetime import datetime
from backend.models.base_model import BaseModel
from sqlalchemy import Column, DATETIME, String


class Log(BaseModel):
    __tablename__ = 'log'
    timestamp = Column(String)
    operation = Column(String)
    description = Column(String)

    def __init__(self, operation: str, description: str):
        date = datetime.now()
        date_formated = date.strftime("%d/%m/%Y %H:%M:%S")
        self.timestamp = date_formated
        self.operation = operation
        self.description = description
from _datetime import datetime
from backend.models.base_model import BaseModel
from sqlalchemy import Column, DATETIME, String
from sqlalchemy.orm import validates


class Log(BaseModel):
    __tablename__ = 'log'
    timestamp = Column(String(length=20), nullable=False)
    operation = Column(String(length=20), nullable=False)
    description = Column(String(length=300), nullable=False)

    def __init__(self, operation: str, description: str):
        self.timestamp = datetime.now()
        self.operation = operation
        self.description = description

    @validates('timestamp')
    def validate_timestamp(self, key, date):
        try:
            date_formated = date.strftime("%d/%m/%Y %H:%M:%S")
            return date_formated
        except ValueError as valError:
            raise ValueError("Error trying to format timestamp!") from valError

    @validates('operation')
    def validate_operation(self, key, operation):
        if operation is None:
            raise ValueError("Log Operation can't be null!")
        elif operation.strip(' ') == '':
            raise ValueError("Log Operation can't contain spaces only!")
        return operation

    @validates('description')
    def validate_description(self, key, description):
        if description is None:
            raise ValueError("Log Operation can't be null!")
        elif description.strip(' ') == '':
            raise ValueError("Log Operation can't contain spaces only!")
        return description

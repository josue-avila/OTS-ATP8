from _datetime import datetime


class Log:
    timestamp: str
    operation: str
    description: str
    id: int

    def __init__(self, operation: str, description: str, id: int = None, timestamp: str = ''):
        if timestamp == '':
            date = datetime.now()
            date_formated = date.strftime("%d/%m/%Y %H:%M:%S")
            self.timestamp = date_formated
        else:
            self.timestamp = timestamp
        self.operation = operation
        self.description = description
        self. id = id

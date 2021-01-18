from _datetime import datetime


class Log:
    __timestamp: str
    __operation: str
    __description: str
    __id: int

    def __init__(self, operation: str, description: str, id: int = None, timestamp: str = ''):
        if timestamp == '':
            date = datetime.now()
            date_formated = date.strftime("%d/%m/%Y %H:%M:%S")
            self.__timestamp = date_formated
        else:
            self.__timestamp = timestamp
        self.__operation = operation
        self.__description = description
        self.__id = id

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

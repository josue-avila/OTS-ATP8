class Marketplace:
    __name: str
    __description: str
    __id: int

    def __init__(self, name: str, description: str, id: int = None):
        self.__name = name
        self.__description = description
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

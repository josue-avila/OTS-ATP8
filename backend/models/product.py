class Product:
    __name: str
    __description: str
    __price: float
    __id: int

    def __init__(self, name: str, description: str, price: float, id: int = None):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @property
    def id(self) -> int:
        return self.__id

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

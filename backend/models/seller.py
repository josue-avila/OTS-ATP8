class Seller:
    __fullname: str
    __phone: str
    __email: str
    __id: int

    def __init__(self, fullname: str, phone: str, email: str, id: int = None):
        self.__fullname = fullname
        self.__phone = phone
        self.__email = email
        self.__id = id

    @property
    def fullname(self) -> str:
        return self.__fullname
    
    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email(self) -> str:
        return self.__email

    @property
    def id(self) -> int:
        return self.__id

    @fullname.setter
    def fullname(self, fullname: str) -> None:
        self.__fullname = fullname

    @phone.setter
    def phone(self, phone: str) -> None:
        self.__phone = phone
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

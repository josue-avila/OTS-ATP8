class Seller:
    fullname: str
    phone: str
    email: str
    id: int

    def __init__(self, fullname: str, phone: str, email: str, id: int = None):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.id = id
class Category:
    name: str
    description: str
    id: int

    def __init__(self, name: str, description: str, id: int=None):
        self.name = name
        self.description = description
        self.id = id

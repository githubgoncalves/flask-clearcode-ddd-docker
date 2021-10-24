""" Models Users """


class Users:
    """Model Users"""

    def __init__(self, id: int, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password
from sqlalchemy import Column, String, Integer
from api.infra.config import Base


class Users(Base):
    """ Users Entity """

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.password == other.password
        ):
            return True
        return False
        
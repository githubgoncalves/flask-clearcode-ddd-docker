from abc import ABC, abstractmethod
from typing import List
from api.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface user repostory"""

    @abstractmethod
    def insert(self, name: str, password: str) -> Users:
        """abstractmethod"""
        raise NotImplementedError

    @abstractmethod
    def select(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstractmethod"""
        raise NotImplementedError
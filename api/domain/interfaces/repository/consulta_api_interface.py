from abc import ABC, abstractmethod
from typing import List


class ConsultaAPIInterface(ABC):
    """Interface Consulta API repository"""

    @abstractmethod
    def consulta_api(self, url: str) -> List:
        """abstractmethod"""
        raise NotImplementedError

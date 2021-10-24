from typing import Dict, List
from abc import ABC, abstractclassmethod


class ConsultaAPI(ABC):
    """ Interface to Consulta API Externa use case """

    @abstractclassmethod
    def consulta_api(cls, url: str) -> List:
        """ Case """

        

        raise Exception("Should implement method: register")
from api.domain.use_cases import ConsultaAPI as ConsultaAPIInterface
from api.domain.interfaces.repository.consulta_api_interface import ConsultaAPIInterface as ConsultaAPIRepository
from typing import List, Type, Dict


class ConsultaAPIService(ConsultaAPIInterface):
    """Class to define usecase: Register User"""

    def __init__(self, consulta_api_repository: Type[ConsultaAPIRepository]) -> None:
        self.consulta_api_repository = consulta_api_repository

    def consulta_api(self, url: str) -> List:
        """Register user use case
        :param - name: person name
               - password: password of the person
        :return - Dictionary with information of the process
        """

        response = None
        validate_entry = isinstance(url, str)

        if validate_entry:
            response = self.consulta_api_repository.consulta_api(url)
        return {"Success": validate_entry, "Data": response}
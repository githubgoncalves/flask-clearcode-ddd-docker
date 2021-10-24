from typing import List
import requests


class ConsultaAPI():
    """Class to manage Consulta API"""

    def consulta(url) -> List:
        """ url de teste "https://615ce36cc29813001773634d.mockapi.io/api/apiDoc/dados" """

        r = requests.get(url)
        dados = r.json()

        return  {"Success": True, "Data": dados}

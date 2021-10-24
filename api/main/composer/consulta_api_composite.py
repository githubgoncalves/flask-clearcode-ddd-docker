"""Design Pattern """
from api.application.presenters.controllers import ConsultaAPIController
from api.domain.services import ConsultaAPIService
from api.infra.repository import ConsultaAPI


def consulta_api_composer():
    """Composing Register Consulta API Route
    :param - None
    :return - Object with  Consulta API Route
    """

    repository = ConsultaAPI()
    
    use_case = ConsultaAPIService(repository)
    register_user_route = ConsultaAPIController(use_case)

    return register_user_route
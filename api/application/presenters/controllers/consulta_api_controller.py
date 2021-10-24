from typing import Type
from api.domain.use_cases import ConsultaAPI as ConsultaAPIInterface
from api.domain.services import ConsultaAPIService
from api.infra.repository import ConsultaAPI
from api.application.presenters import HttpRequest, HttpResponse, HttpErrors


class ConsultaAPIController():
    """Class to Define Route to consulta_api use case"""

    def __init__(self, consulta_api_use_case: Type[ConsultaAPIService]):
        self.consulta_api_use_case = consulta_api_use_case

        self.consulta_api = ConsultaAPI()

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call consulta_api case"""

        response = None

        if http_request.body:
            # if body in htp_request

            body_params = http_request.body.keys()

            if "url" in body_params:
                url = http_request.body["url"]

                if (url != '' and url != None):
                    response = ConsultaAPI().consulta(url)
                else:
                    url = http_request.header["url"]
                    response = ConsultaAPI.consulta(url)
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
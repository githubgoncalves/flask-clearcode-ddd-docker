"""Design Pattern """
from api.application.presenters.controllers import RegisterUserController
from api.domain.services import RegisterUser
from api.infra.repository import UserRepository


def register_user_composer():
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
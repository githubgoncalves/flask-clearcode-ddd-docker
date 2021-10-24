from api.application.presenters.controllers import FindUserController
from api.domain.services import FindUser
from api.infra.repository.users_repository import UserRepository


def find_user_composer() -> FindUserController:
    """Composing Find User Route
    :param - None
    :return - Object with Find User Route
    """

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
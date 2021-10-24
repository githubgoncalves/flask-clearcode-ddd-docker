from api.domain.use_cases import RegisterUser as RegisterUserInterface
#from api.domain.interfaces.repository.user_repository_interface import UserRepositoryInterface as UserRepository
from api.domain.models import Users
from api.infra.repository.users_repository import UserRepository
from typing import Type, Dict


class RegisterUser(RegisterUserInterface):
    """Class to define usecase: Register User"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        #self.user_repository = user_repository
        self.user_repository = UserRepository()

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case
        :param - name: person name
               - password: password of the person
        :return - Dictionary with information of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert(name, password)
        return {"Success": validate_entry, "Data": response}
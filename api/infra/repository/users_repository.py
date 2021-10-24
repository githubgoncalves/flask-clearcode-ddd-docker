""" Repository to User Entity """
from api.domain.models import Users
from api.infra.config import DBConnectionHandler
from api.infra.entities import users_entities as UsersModel
from api.domain.interfaces.repository import UserRepositoryInterface
from typing import List


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert(cls, name: str, password: str) -> None:
        """Insert data in user entity
        :param - name: person name
               - password: person password
        :return - tuple with new user
        """
        with DBConnectionHandler() as db_connection: 
            try:
                new_user = UsersModel.Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except Exception as exc:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
        Select data in user entity by id and/or name
        :param - user_id: Id of the registry
               - name: Person name
        :return - List of Users
        """
        try:
            query_data = None
            if user_id and not name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    ) 
                    query_data = [data]

            return query_data

        except:
            
            raise

        finally:
            db_connection.session.close()

        return None
        
from api.infra.config.db_config import DBConnectionHandler
from sqlalchemy import MetaData,Table,Column,Integer,String
from api.infra.entities.users_entities import Users
from api.infra.config import db_base

class CreateDataBase():

    def __init__(self):
    
        self.engine = DBConnectionHandler().get_engine()

        metadata = MetaData()

        users = Table('Users', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(80), nullable=False),
            Column('password', String(80), nullable=False)
        )

        metadata.create_all(self.engine,checkfirst=True)

        


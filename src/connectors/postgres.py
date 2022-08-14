from connectors.base import DBConnector
from exception_handlers.connector_handler import handler


class PostGres(DBConnector):

    def __init__(self):
        try:
            super().__init__('postgres')
            print(f"DB Config is : {self.db_config}")
        except Exception as err:
            handler()
            raise Exception(f"Error while creating connection string for postgres, following is the error\n{str(err)}")
        pass

    def __make_connection_string(self):
        pass

    def __create_connection_object(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def run(self, query):
        pass

from connector import DBConnector
from exception_handlers.connector_handler import handler


class PostGres(DBConnector):

    def __init__(self):
        try:
            DBConnector.__init__(self, 'postgres')
            print(DBConnector.conn_string)
        except Exception:
            handler()
            raise Exception(f"Error while creating connection string for postgres DB")

        pass

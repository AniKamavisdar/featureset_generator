from connector import DBConnector
from exception_handlers.connector_handler import handler


class BigQuery(DBConnector):

    def __init__(self):
        try:
            DBConnector.__init__(self, 'bigquery')
            print(DBConnector.conn_string)
        except Exception:
            raise f"Error while creating connection string for postgres DB"
        finally:
            handler()
        pass

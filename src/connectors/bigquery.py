from connectors.connector import DBConnector


class BigQuery(DBConnector):

    def __init__(self):
        try:
            super().__init__('big_query')
            print(f"DB CONFIG IS : {self.db_config}")
        except Exception as err:
            raise Exception(f"Error while creating connection string for Bigquery, following is the error\n{str(err)}")

    def __make_connection_string(self):
        pass

    def __create_connection_object(self):
        pass

from configs.connector_config import conf


class DBConnector:
    conn_string = None

    def __init__(self, conn_type):
        self.db_config = conf.connector_configs[conn_type]
        self.__populate_conn_string(self.db_config)

    def __populate_conn_string(self, db_config):
        self.conn_string = db_config.conn_string


class FileConnector:
    conn_string = None

    def __init__(self, conn_type):
        self.db_config = conf.connector_configs[conn_type]
        self.__populate_conn_string(self.db_config)

    def populate_conn_string(self, db_config):
        self.conn_string = db_config.conn_string

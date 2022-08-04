from configs.connector_config import static_config


class DBConnector:

    def __init__(self, conn_type):
        self.conn_type = conn_type
        self.db_config = static_config.connector_configs[conn_type]
        self.connection_obj = None


class FileConnector:
    conn_string = None

    def __init__(self, conn_type):
        self.conn_type = conn_type
        self.db_config = static_config.connector_configs[conn_type]

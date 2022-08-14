from configs.static import static_config
from abc import ABC, abstractmethod


class DBConnector(ABC):

    def __init__(self, conn_type):
        self.conn_type = conn_type
        self.db_config = static_config.connector_configs[conn_type]
        self.connection_obj = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def run(self, logic):
        pass


class FileConnector:
    conn_string = None

    def __init__(self, conn_type):
        self.conn_type = conn_type
        self.db_config = static_config.connector_configs[conn_type]

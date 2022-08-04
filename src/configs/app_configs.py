import getopt
import sys


def get_config_env():
    """Logic to dynamically detect environment based on server values to go here.
    Let's say all servers would have environment variables which tells the type of env
    Variable Name could be 'ENVIRONMENT', we can then extract using 'os.env' command and set our config.
    Making this method unit testable and configurable"""
    return 'dev'


class AppConfig:
    """
    All the parameters required by the AppConfig will be populated by the MasterService.
    This will ensure that only one instance of a single type of service request is running.
    All the services will be tracked by master. (By Mechanism?)
    """

    app_name = None

    # lower_limit = 5431
    # upper_limit = 5440

    def __init__(self, app_name='featureset_generator', port=5341, host='0.0.0.0', version=get_config_env()):
        self.env = get_config_env()
        self.app_name = app_name
        self.port = port  # self.__get_port(port)
        self.host = host
        self.version = version
        self.__get_runtime_arguments()

    def __get_runtime_arguments(self):
        try:
            argument_list = sys.argv[1:]
            options = "a:p:h:v:c:f:t:"
            long_options = ["app_name=", "port=", "host=", "version=", "connector=", "function=", "function_type="]
            arguments, values = getopt.getopt(argument_list, options, long_options)

            for curr_arg, curr_val in arguments:
                if curr_arg in ("-a", "--app_name"):
                    self.app_name = curr_val
                elif curr_arg in ("-p", "--port"):
                    self.port = curr_val
                elif curr_arg in ("-h", "--host"):
                    self.host = curr_val
                elif curr_arg in ("-v", "--version"):
                    self.version = curr_val
        except getopt.error as err:
            raise Exception(str(err))

    # def __get_port(self, port):
    #     if self.__is_valid_port_for_app(port):
    #         return port
    #     else:
    #         return None
    #
    # @staticmethod
    # def __is_valid_port_for_app(port):
    #     return True if port in range(self.lower_limit, self.upper_limit) else False


app_config = AppConfig()

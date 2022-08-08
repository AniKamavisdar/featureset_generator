import getopt
import sys

# Importing connector parsers and function parsers
from connectors import bigquery, postgres  # , json_file, gcp_bucket
from data.transformers import pkl_transformer, py_transformer, py_obj_transformer, passthrough_transformer


class JobConfig:
    """
    All the parameters parsed and utilised in the JobConfig will be user driven.

    This will give the user the flexibility to customise the service based on the availability and support.

    Version1 Supports:
    Connectors: BigQuery | PgSQL | CSV File
    Custom Function: Py File | Py Module as String

    Future Scope:
    Connectors: MySql | MongoDB | Json
    Custom Function: R File | R Module as string
    """

    def __init__(self):
        # self.run_date = datetime.datetime.today()
        self.__get_runtime_arguments()
        self.__get_connector(self.connector_type)
        self.__get_transformer(self.function_type)

    def __get_runtime_arguments(self):
        try:
            argument_list = sys.argv[1:]
            options = "a:p:h:v:c:t:f:e:"
            long_options = ["app_name=", "port=", "host=", "version=", "connector=", "function=",
                            "function_type=", "extractor_logic="]
            arguments, values = getopt.getopt(argument_list, options, long_options)
            for curr_arg, curr_val in arguments:
                if curr_arg in ("-c", "--connector"):
                    self.connector_type = curr_val
                elif curr_arg in ("-f", "--function"):
                    self.function_module = curr_val
                elif curr_arg in ("-t", "--function_type"):
                    self.function_type = curr_val
                elif curr_arg in ("-e", "--extractor_logic"):
                    self.extractor_logic = curr_val
        except getopt.error as err:
            raise Exception(str(err))

    def __get_connector(self, conn_type):
        """
        WARNING : This function is internal to the class,
        should not be used to call externally as it hierarchical to previous statements.

        The function is supposed to use the runtime arguments to create connector base.
        This would serve to create run multiple instance of this job with different configurations,
        Allowing the ability to connector to multiple sources driven by configuration.

        :param conn_type:
        :return:
        """
        if conn_type == 'big_query':
            self.connector = bigquery.BigQuery()
        elif conn_type == 'postgres':
            self.connector = postgres.PostGres()
        elif conn_type == 'csv_connector':
            raise Exception(f"{conn_type} is not yet defined, implementation in progress.")
        else:
            raise Exception(f"{conn_type} is not valid connector type supported by application...")

    def __get_transformer(self, function_type):
        """
        WARNING : This function is internal to the class,
        should not be used to call externally as it hierarchical to previous statements.
        
        The function is supposed to use runtime arguments to create transformer base.
        This would serve to create run multiple instance of this job with different configurations,
        Allowing the ability to parse external logic.
        
        :param function_type:
        :return:
        """
        if function_type == 'pkl':
            self.transformer = pkl_transformer.PklTransformer()
        elif function_type == 'py_file':
            self.transformer = py_transformer.PyFileTransformer()
        elif function_type == 'py_method':
            self.transformer = py_obj_transformer.PyObjTransformer()
        elif function_type == 'passthrough':
            self.transformer = passthrough_transformer.Passthrough()
        elif function_type == 'r_file':
            raise Exception(f"{function_type} is not yet defined, implementation in progress.")
        elif function_type == 'r_method':
            raise Exception(f"{function_type} is not yet defined, implementation in progress.")
        else:
            raise Exception(f"{function_type} is not valid connector type supported by application...")


job_config = JobConfig()

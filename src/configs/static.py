class StaticConfig:
    connector_configs = {'big_query': "BIGQUERYCONNECTION",
                         'postgres': "POSTGRESCONNECTION",
                         'csv_connector': "CSVCONNECTION",
                         'api_connector': "API_CONNECTIOR",
                         'gcp_bucket': "GCPBUCKET"
                         }

    function_configs = {'pkl': "PickelTypeFunction",
                        'py_file': "PythonFileFunction",
                        'py_method': "PythonMethod",
                        'passthrough': "PassThrough",
                        'r_file': "RFileFunction",
                        'r_method': "RMethod"}


static_config = StaticConfig()

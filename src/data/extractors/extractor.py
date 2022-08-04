from configs.connector_config import static_config


class Extractor:
    """
    The extractors will get executed with the baseline assumption that necessary required libraries will be installed
    on the VM evn before the program execution starts.

    It will be the key responsibility of the Master service to ensure that that requirements are checked and
    installed if any missing before starting the featureset generator app
    """

    def __init__(self, function_type):
        self.function_type = function_type
        self.function = static_config.function_configs[function_type]
        self.extractor_object = None

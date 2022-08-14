from abc import ABC, abstractmethod
from configs.static import static_config

class Transformer(ABC):
    """
    The transformer will get executed with the baseline assumption that necessary required libraries will be installed
    on the VM evn before the program execution starts.

    It will be the key responsibility of the Master service to ensure that that requirements are checked and
    installed if any missing before starting the featureset generator app
    """

    def __init__(self, function_type):
        self.function_type = function_type
        self.function = static_config.function_configs[function_type]
        self.transformer_object = None

    @abstractmethod
    def load_transformer(self, params=None):
        pass

from abc import ABC, abstractmethod


class Extractor(ABC):
    def __init__(self, ext_type):
        self.ext_type = ext_type
        self.ext_logic = None

    @abstractmethod
    def set_ext_logic(self, param):
        pass

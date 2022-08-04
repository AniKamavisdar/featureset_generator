from data.extractors.extractor import Extractor


class PyObjExtractor(Extractor):

    def __init__(self):
        super().__init__('py_method')

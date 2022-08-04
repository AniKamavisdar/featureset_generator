from data.extractors.extractor import Extractor


class PyFileExtractor(Extractor):

    def __init__(self):
        super().__init__('py_file')

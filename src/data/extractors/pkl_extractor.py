from data.extractors.extractor import Extractor


class PklExtractor(Extractor):

    def __init__(self):
        super().__init__('pkl')
        print(f"Extractor is {self.function_type}")

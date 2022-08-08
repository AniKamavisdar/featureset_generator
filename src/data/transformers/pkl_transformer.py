from data.transformers.transformer import Transformer


class PklTransformer(Transformer):

    def __init__(self):
        super().__init__('pkl')

    def load_transformer(self):
        pass

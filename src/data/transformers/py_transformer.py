from data.transformers.transformer import Transformer


class PyFileTransformer(Transformer):

    def __init__(self):
        super().__init__('py_file')

    def load_transformer(self):
        pass

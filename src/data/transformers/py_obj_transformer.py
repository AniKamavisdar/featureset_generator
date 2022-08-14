from data.transformers.transformer import Transformer


class PyObjTransformer(Transformer):

    def __init__(self):
        super().__init__('py_method')

    def load_transformer(self, file_name=None):
        pass

from data.transformers.transformer import Transformer
from package import Transformer_


class PyFileTransformer(Transformer):

    def __init__(self):
        super().__init__('py_file')

    def load_transformer(self,file_name=None):
        self.transformer_object = Transformer_()

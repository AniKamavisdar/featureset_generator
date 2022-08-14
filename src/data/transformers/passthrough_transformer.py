from data.transformers.transformer import Transformer


class Passthrough(Transformer):
    def __init__(self):
        super().__init__('passthrough')

    def load_transformer(self, file_name):
        self.transformer_object = self.pass_through

    @staticmethod
    def pass_through(*args):
        return args

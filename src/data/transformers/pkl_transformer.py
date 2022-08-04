from data.transformers.transformer import Transformer


class PklTransformer(Transformer):

    def __init__(self):
        super().__init__('pkl')
        print(f"Transformer is {self.function_type}")

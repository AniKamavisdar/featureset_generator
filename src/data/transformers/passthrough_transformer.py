from data.transformers.transformer import Transformer


class Passthrough(Transformer):
    def __init__(self):
        super().__init__('passthrough')
        print(f"Transformer is {self.function_type}")
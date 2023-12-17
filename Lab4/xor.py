import math

class BackPropagation:
    def __init__(self) -> None:
        pass

    def get_sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def get_derivate_sigmoid(self, x):
        return x * (1 - x)

if __name__ == '__main__':
    bp = BackPropagation()

    print('Hello World!')
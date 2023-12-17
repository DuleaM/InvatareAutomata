import math
from random import random


class BackPropagation:
    input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    output = [[0], [1], [1], [0]]

    def __init__(self) -> None:
        self.output = []
        self.hidden = [random() for _ in range(2)]
        self.hidden_prag = [random() for _ in range(2)]
        self.weights_input_hidden = [[random() for _ in range(2)] for __ in range(2)]
        self.weights_output_hidden = [[random() for _ in range(1)] for __ in range(2)]

    def get_sigmoid(self, x) -> float:
        return 1 / (1 + math.exp(-x))

    def get_derivate_sigmoid(self, x) -> float:
        return x * (1 - x)

    def train_model(self) -> None:
        pass

    def main():
        pass

if __name__ == '__main__':
    bp = BackPropagation()

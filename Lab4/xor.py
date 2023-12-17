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
        error = 0
        while error < 0.001:
            for i in range(len(self.input)):
                self.forward_propagation(i)
                self.back_propagation(i)

    def forward_propagation(self, i) -> int:
        input = [self.input[i][0], self.input[i][1]]
        output = 0

        for j in range(len(self.hidden)):
            self.hidden[j] = input[0] * self.weights_input_hidden[0][j] + input[1] * self.weights_input_hidden[1][j]
            self.hidden[j] = self.get_sigmoid(self.hidden[j])

        for j in range(len(self.output)):
            output += self.weights_output_hidden[j] * self.hidden[j]

        error = (self.output[i][0] - output) ** 2
        return error

    def back_propagation(self, i) -> None:
        pass

    def main(self, x, y):
        output = 0
        outputPrag = 0

        for i in range(2):
            self.hidden[i] = x * self.weights_input_hidden[0][i] + y * self.weights_input_hidden[1][i]
            self.hidden[i] = self.get_sigmoid(self.hidden[i])

        for i in range(2):
            output += self.weights_output_hidden[i] * self.hidden[i]

        output = self.get_sigmoid(output + outputPrag)

if __name__ == '__main__':
    bp = BackPropagation()
    bp.train_model()
    print(bp.main())

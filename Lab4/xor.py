import math
from random import random


class BackPropagation:
    input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    output = [[0], [1], [1], [0]]

    def __init__(self) -> None:
        self.hidden = [random() for _ in range(2)]
        self.hidden_prag = [random() for _ in range(2)]
        self.weights_input_hidden = [[random() for _ in range(2)] for __ in range(2)]
        self.weights_output_hidden = [[random() for _ in range(1)] for __ in range(2)]
        self.output_prag = random()
        
    def get_sigmoid(self, x) -> float:
        return 1 / (1 + math.exp(-x))

    def get_derivate_sigmoid(self, x) -> float:
        return x * (1 - x)

    def train_model(self) -> None:
        error = 0
        while error > 0.001:
            for i in range(len(self.input)):
                output, error = self.forward_propagation(i)
                self.back_propagation(i, output)

    def forward_propagation(self, i) -> int:
        input = [self.input[i][0], self.input[i][1]]
        output = 0

        for j in range(2):
            self.hidden[j] = input[0] * self.weights_input_hidden[0][j] + input[1] * self.weights_input_hidden[1][j]
            self.hidden[j] = self.get_sigmoid(self.hidden[j])

        for j in range(2):
            output += self.weights_output_hidden[j][0] * self.hidden[j]

        output = self.get_sigmoid(output + self.output_prag)
        error = (self.output[i][0] - output) ** 2
        
        return output, error

    def back_propagation(self, i, output) -> None:
        for j in range(2):
            self.weights_output_hidden[j][0] += 0.1 * (self.output[i][0] - output) * self.hidden[j] * self.get_derivate_sigmoid(output)
            
        for j in range(2):
            for k in range(2):
                self.weights_input_hidden[j][k] += 0.1 * (self.output[i][0] - output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(output) * self.get_derivate_sigmoid(self.hidden[j]) * self.input[i][k]
                self.hidden_prag[j] += 0.1 * (self.output[i][0] - output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(output) * self.get_derivate_sigmoid(self.hidden[j])
    
    def predict(self, x, y):
        output = 0
        outputPrag = 0

        for i in range(2):
            self.hidden[i] = x * self.weights_input_hidden[0][i] + y * self.weights_input_hidden[1][i]
            self.hidden[i] = self.get_sigmoid(self.hidden[i])

        for i in range(2):
            output += self.weights_output_hidden[i][0] * self.hidden[i]

        output = self.get_sigmoid(output + outputPrag)

        return output

    def main(self):
        pass
if __name__ == '__main__':
    bp = BackPropagation()
    
    bp.train_model()
    
    if(bp.predict(0, 0) < 0.5):
        print("0")
    else:
        print("1")
    
    if(bp.predict(0, 1) < 0.5):
        print("0")
    else:
        print("1")
    
    if(bp.predict(1, 0) < 0.5):
        print("0")
    else:
        print("1")
    
    if(bp.predict(1, 1) < 0.5):
        print("0")
    else:
        print("1")

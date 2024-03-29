import math
from random import random


class BackPropagation:
    input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    output = [[0], [1], [1], [0]]

    def __init__(self) -> None:
        self.hidden = [0, 0] #hidden layer
        self.output_prag = random() #prag output
        self.hidden_prag = [random() for _ in range(2)] #prag hidden
        self.weights_input_hidden = [[random() for _ in range(2)] for __ in range(2)] #ponderi conexiuni input-hidden
        self.weights_output_hidden = [[random() for _ in range(1)] for __ in range(2)] #ponderi conexiuni hidden-output
        self.epochs_max = 100000
        self.epochs = self.epochs_max

    def print_variables(self):
        print("hidden:", self.hidden)
        print("output_prag:", self.output_prag)
        print("hidden_prag:", self.hidden_prag)
        print("weights_input_hidden:", self.weights_input_hidden)
        print("weights_output_hidden:", self.weights_output_hidden)
        
    def get_sigmoid(self, x) -> float:
        return 1. / (1. + math.exp(-x))

    def get_derivate_sigmoid(self, x) -> float:
        return x * (1. - x)

    def train_model(self) -> None:
        error = 1
        while error > 0.001 and self.epochs != 0:
            for i in range(len(self.input)):
                input = [self.input[i][0], self.input[i][1]]
                
                output, error = self.forward_propagation(i, input)
                self.back_propagation(i, input, output)
            
            self.epochs -= 1
            print(error)

    def forward_propagation(self, i, input) -> int:
        output = self.predict(input[0], input[1])
        
        error = (output - self.output[i][0]) ** 2
        
        return output, error

    def predict(self, x, y):
        output = 0
        for i in range(2):
            self.hidden[i] = self.get_sigmoid(x * self.weights_input_hidden[0][i] + y * self.weights_input_hidden[1][i] + self.hidden_prag[i])
        
        for i in range(2):
            output += self.weights_output_hidden[i][0] * self.hidden[i]

        output = self.get_sigmoid(self.output_prag + output)


        return output
    
    def back_propagation(self, i, input, output) -> None:
        coef = 0.8
        self.output_prag = self.output_prag - coef * (2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output))
        
        #input - hidden
        for j in range(2):
            self.hidden_prag[j] -= coef * 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j])
            self.weights_input_hidden[0][j] -= coef * 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j]) * input[0]
            self.weights_input_hidden[1][j] -= coef * 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j]) * input[1]
        
        #hidden - output
        for j in range(2):
            self.weights_output_hidden[j][0] -= coef * 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.hidden[j]



    def main(self):
        pass

if __name__ == '__main__':
    bp = BackPropagation()
    
    bp.train_model()
    print(f'Program finished with {bp.epochs_max - bp.epochs} epochs')
    
    temp = bp.predict(0, 0)
    print(f"0 ^ 0 = {temp}")
    
    temp = bp.predict(0, 1)
    print(f"0 ^ 1 = {temp}")

    temp = bp.predict(1, 0)
    print(f"1 ^ 0 = {temp}")
        
    temp = bp.predict(1, 1)
    print(f"1 ^ 1 = {temp}")


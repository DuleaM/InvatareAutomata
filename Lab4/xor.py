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
        self.epochs = 0

        self.print_variables()
        
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
        while error > 0.001:
            for i in range(len(self.input)):
                input = [self.input[i][0], self.input[i][1]]
                
                output, error = self.forward_propagation(i, input)
                self.back_propagation(i, input, output)
            
            self.epochs += 1
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

        self.output_prag -= 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output)
        
        for j in range(2):
            self.hidden_prag[j] -= 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j])
            self.weights_input_hidden[0][j] -= 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j]) * input[0]
            self.weights_input_hidden[1][j] -= 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.weights_output_hidden[j][0] * self.get_derivate_sigmoid(self.hidden[j]) * input[1]
        
        for j in range(2):
            self.weights_output_hidden[j][0] -= 2 * (output - self.output[i][0]) * self.get_derivate_sigmoid(output) * self.hidden[j]



    def main(self):
        pass

if __name__ == '__main__':
    bp = BackPropagation()
    
    bp.train_model()
    print(f'Program finished with {bp.epochs} epochs')
    
    if(bp.predict(0, 0) >= 0.5):
        print("0 ^ 0 = 1")
    else:
        print("0 ^ 0 = 0")
    
    if(bp.predict(0, 1) >= 0.5):
        print("0 ^ 1 = 1")
    else:
        print("0 ^ 1 = 0")
    
    if(bp.predict(1, 0) >= 0.5):
        print("1 ^ 0 = 1")
    else:
        print("1 ^ 0 = 0")
    
    if(bp.predict(1, 1) >= 0.5):
        print("1 ^ 1 = 1")
    else:
        print("1 ^ 1 = 0")

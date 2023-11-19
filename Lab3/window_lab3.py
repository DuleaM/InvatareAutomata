import matplotlib.pyplot as plt

class Window:
    x = []
    y = []
    
    x_max = 300
    x_min = -x_max

    y_max = 300
    y_min = -y_max
    
    fig, ax = plt.subplots(figsize=(3, 3))
    
    def __init__(self):
        self.ax.set_aspect('equal')

        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.x_max)

        self.ax.set_xticks([])  
        self.ax.set_yticks([])

    def set_points(self, points):
        x = []
        y = []
        
        for point in points:
            x.append(point['x'])
            y.append(point['y'])

        self.draw_points(x, y, color='black', strength=1, label='Points')

    def set_neurons(self, neurons):
        x = []
        y = []
        
        for row in neurons:
            for neuron in row:
                x.append(neuron['x'])
                y.append(neuron['y'])

        self.draw_points(x, y, color='red', strength=10, label='Neurons')

    def draw_points(self, x = [], y = [], color='black', strength=1, label=''):
        self.ax.scatter(x=x, y=y, color=color, marker='o', s=strength, label=label)
        self.ax.legend(color, loc='upper left')

    def open_window(self):
        plt.show()
        plt.grid()
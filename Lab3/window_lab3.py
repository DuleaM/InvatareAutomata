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

        self.draw_points(x, y, color='red', strength=15, label='Neurons')

    def draw_lines(self, neurons):
        for row in neurons:
            xs = []
            ys = []
            
            for neuron in row:
                xs.append(neuron['x'])
                ys.append(neuron['y'])
            
            plt.plot(xs, ys, color='blue', linewidth=0.5)    
            plt.plot(ys, xs, color='blue', linewidth=0.5) 

    def draw_points(self, x = [], y = [], color='black', strength=1, label=''):
        self.ax.scatter(x=x, y=y, color=color, marker='o', s=strength, label=label)
        self.ax.legend(color, loc='upper left')
    
    def open_window(self, block=True):
        plt.show(block=block)
    
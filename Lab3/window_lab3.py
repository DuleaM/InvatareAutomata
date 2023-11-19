import matplotlib.pyplot as plt

class Window:
    x = []
    y = []
    fig, ax = plt.subplots(figsize=(3, 3))
    
    def __init__(self):
        
        self.ax.set_aspect('equal')

        self.ax.set_xlim(-300, 300)
        self.ax.set_ylim(-300, 300)

        self.ax.set_xticks([])  
        self.ax.set_yticks([])


    def set_points(self, points):
        for point in points:
            self.x.append(point['x'])
            self.y.append(point['y'])

    def draw_points(self):
        self.ax.scatter(self.x, self.y, color='black', marker='o', s=1)
        self.ax.legend(loc='upper left')
    
    def open_window(self):
        self.draw_points()
        plt.show()
        plt.grid(True)
        plt.legend()
        
        
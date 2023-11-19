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
        
        self.__get_points()

    def __get_points(self):
        with open('output.txt', 'r') as file:
            for line in file:
                elements = line.split()
                self.x.append(int(elements[0]))
                self.y.append(int(elements[1]))

    def open_window(self):
        plt.show()
        plt.grid(True)
        plt.legend()

if __name__ == '__main__':
    window = Window()
    window.open_window()
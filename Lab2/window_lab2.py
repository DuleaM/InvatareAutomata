
import matplotlib.pyplot as plt
import time

class Window:

    colors = {
        0 : '#FF33B1',
        1 : 'red',
        2 : 'yellow',
        3 : 'green',
        4 : 'blue',
        5 : 'purple',
        6 : 'cyan',
        7 : 'magenta',
        8 : 'orange',
        9 : '#33FFC8'
    }

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


    def draw_points(self, x=[], y=[], color='black', thickness=1 ,label=None):

        self.ax.scatter(x, y, color=color, marker='o', s=thickness, label = label)
        self.ax.legend(loc='upper left')


    def open_window(self):
        plt.show(block=False)
        plt.grid(True)
        plt.legend()

if __name__ == '__main__':
    window = Window()
    window.open_window()




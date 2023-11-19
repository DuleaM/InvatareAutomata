from window_lab3 import Window

class SOM:
    
    def __init__(self) -> None:
        self.points = self.__get_coordinates()
        self.neurons = self.__get_neurons()
        # setting up the window
        self.window = Window()
        self.window.set_points(self.points)

    def __get_coordinates(self): 
        points = []
        with open('output.txt', 'r') as file:
            for line in file:
                elements = line.split()
                x = int(elements[0])
                y = int(elements[1])
                
                coords = {'x': x, 'y': y}
                
                points.append(coords)
        
        return points

    def __get_neurons(self):
        neurons = []

        for row in range(10):
            r = []
            for col in range(10):
                x = -300 + col * 60  # Adjust the scaling factor as needed
                y = -300 + row * 60  # Adjust the scaling factor as needed
                
                coords = {'x': x, 'y': y}
                r.append(coords)
                
            neurons.append(r)
        
        return neurons

    def main(self):
        self.window.open_window()


if __name__ == '__main__':
    som = SOM()
    som.main()
        
    def main(self):
        self.window.open_window()


if __name__ == '__main__':
    som = SOM()
    som.main()
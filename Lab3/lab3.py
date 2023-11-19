from window_lab3 import Window, plt

class SOM:
    
    def __init__(self) -> None:
        # setting up the window
        self.window = Window()
        
        # setting up the coordinates
        self.points = self.__get_coordinates()
        self.neurons = self.__get_neurons()

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
                x = 30 + self.window.x_min + col * 60  # Adjust the scaling factor as needed
                y = 30 + self.window.y_min + row * 60  # Adjust the scaling factor as needed
                
                coords = {'x': x, 'y': y}
                r.append(coords)
                
            neurons.append(r)
        
        return neurons

    def draw_plot(self, refresh=False):
        if refresh:
            self.window.clear_window()
            
        self.window.set_points(self.points)
        self.window.set_neurons(self.neurons)
        self.window.draw_lines(self.neurons)

    def main(self):
        self.window.open_window(block=False)
        
        self.draw_plot(refresh=True)
        
        self.window.open_window()

if __name__ == '__main__':
    som = SOM()
    som.main()

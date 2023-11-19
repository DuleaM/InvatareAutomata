from window_lab3 import Window

class SOM:
    
    def __init__(self) -> None:
        self.points = self.__get_coordinates()
        self.neurons = []
        #setting up the window
        self.window = Window()
        self.window.set_points(self.points)

    def __get_coordinates(self): 
        points = []
        with open('output.txt', 'r') as file:
            for line in file:
                elements = line.split()
                x = int(elements[0])
                y = int(elements[1])
                
                coords = {'x' : x, 'y' : y}
                
                points.append(coords)
        
        return points

    def __get_neurons():
        
    def main(self):
        self.window.open_window()


if __name__ == '__main__':
    som = SOM()
    som.main()
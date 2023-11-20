import sys
import math
from window_lab3 import Window



class SOM:
    """LEGEND
    
    pondere = pozitia unui neuron in spatiul de reprezentare
    vector de intrare = punctul din spatiul de intrare
    alfa(t) = coeficientul de invatare la pasul t
    calculul vecinatatii ->
    
    N -> este dat de noi ?
    
    
    calculam prima data invingator intre neuron si punct
    dupa mutam neuronul vecin cu aceeasi formula dupa neuronul invingator
    vecin se considera orice punct din domeniul [i-v, i+v] şi [j-v, j+v], unde V
    """
    def __init__(self) -> None:
        # setting up the window
        self.window = Window()
        
        # setting up the coordinates
        self.points = self.__get_coordinates()
        self.neurons = self.__get_neurons()

        # setting up the other vars
        self.length = 10 # range of matrix
        self.N = 100 #total number of steps
        self.T = 1 #step
        
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

        for row in range(self.length):
            r = []
            for col in range(self.length):
                x = 30 + self.window.x_min + col * 60 
                y = 30 + self.window.y_min + row * 60
                
                coords = {'x': x, 'y': y}
                r.append(coords)
                
            neurons.append(r)
        
        return neurons

    def draw_plot(self, refresh=False):
        """Draw the plot with the points and neurons

        Args:
            refresh (bool, optional): If set to true, the old plot will be deleted. Defaults to False.
        """
        
        if refresh:
            self.window.clear_window()
            
        self.window.set_points(self.points)
        self.window.set_neurons(self.neurons)
        self.window.draw_lines(self.neurons)

    def get_distance(self, point, neuron):
        """Get Euclidian Distance between a point and a neuron

        Args:
            point (dict): contains x and y of the point
            neuron (dict): contains x and y of the neuron

        Returns:
            float: the distance between the point and the neuron
        """

        xs = (point['x'] - neuron['x']) ** 2
        ys = (point['y'] - neuron['y']) ** 2
        
        return math.sqrt(xs + ys)

    def replace_closest_neuron(self):

        for point in self.points:
            min_distance = sys.maxsize
            closest_neuron = None
            
            for row in self.neurons:
                for neuron in row:
                    distance = self.get_distance(point, neuron)
                
                    if distance < min_distance:
                        min_distance = distance
                        closest_neuron = neuron

            self.replace_neuron(closest_neuron)

    def replace_neuron(self, neuron):
        pass
    
    def update_point(self, winner, point):
        pass
    
    def get_neighbourhood(self, x, y):
        coeficient = self.get_afla_T()
        
        height = int(x + coeficient) 
        width = int(y + coeficient)

        
    def __normalizare(self, n):
        pass
    
    def get_afla_T(self):
        return 0.6 * math.pow(math.e, - (self.T / self.N))
    
    def get_neighbour_T(self):
        return 6.1 * math.pow(math.e, - (self.T / self.N)) + 1

    def main(self):
        self.window.open_window(block=False)
            
        self.draw_plot(refresh=True)
        self.replace_closest_neuron()
        
        self.window.open_window()

if __name__ == '__main__':
    som = SOM()
    som.main()
    
    som.get_neighbourhood()

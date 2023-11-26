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
        # setting up the other vars
        self.length = 10 # range of matrix
        self.N = 10 #total number of steps
        self.T = 1 #step

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
        """ We go through all the points and we replace the closest neuron coordinates

        """

        for point in self.points:
            min_distance = sys.maxsize
            winner_neuron= None

            for i, row in enumerate(self.neurons):
                for j, neuron in enumerate(row):
                    distance = self.get_distance(point, neuron)

                    if distance < min_distance:
                        min_distance = distance
                        winner_neuron = (i, j)

            # here we replace the winner neuron coordinates
            new_winner_coordinates = self.get_new_coordinates(point, self.neurons[winner_neuron[0]][winner_neuron[1]])
            self.neurons[winner_neuron[0]][winner_neuron[1]] = new_winner_coordinates


            #here we replace the neighbours coordinates
            neighbours = self.get_neighbourhood(winner_neuron[0], winner_neuron[1])
            for neighbour_coordinates in neighbours:

                neighbour = self.neurons[neighbour_coordinates[0]][neighbour_coordinates[1]]
                neighbour_new_coordinates = self.get_new_coordinates(new_winner_coordinates, neighbour)
                self.neurons[neighbour_coordinates[0]][neighbour_coordinates[1]] = neighbour_new_coordinates

            self.draw_plot(refresh=True)

    def get_new_coordinates(self, point, neuron):
        alfa_t = self.get_afla_T()

        new_x = neuron['x'] + alfa_t * (point['x'] - neuron['x'])
        new_y = neuron['y'] + alfa_t * (point['y'] - neuron['y'])

        return {'x': new_x, 'y': new_y}

    def get_neighbourhood(self, i, j):
        neigbourhood_coeficient = self.get_neighbour_T()
        neighbours=[]

        for coeficinet in range(1, neigbourhood_coeficient):
            area_neighbourhood = self.__get_neighbours(i, j, coeficinet)
            neighbours.extend(area_neighbourhood)

        return neighbours

    def __get_neighbours(self, i, j, coeficient):
        neighbours = []
        height_up, height_down = i + coeficient, i - coeficient
        width_right, width_left = j + coeficient, j - coeficient

        for row in range(height_down, height_up + 1):
            for col in range(width_left, width_right + 1):
                if row == i and col == j:
                    continue

                if row < 0 or row >= self.length:
                    continue

                if col < 0 or col >= self.length:
                    continue

                neighbours.append((row, col))

        return neighbours


    def get_afla_T(self):
        return 0.6 * math.pow(math.e, - (self.T / self.N))

    def get_neighbour_T(self):
        """Get Neighbourhood Coeficient

        Returns:
            float: the neighbourhood coeficient
        """

        return int(6.1 * math.pow(math.e, - (self.T / self.N)) + 1)


    def main(self):
        self.window.open_window(block=False)

        self.draw_plot(refresh=True)
        self.get_neighbourhood(4, 4)
        self.replace_closest_neuron()

        self.window.open_window()

if __name__ == '__main__':
    som = SOM()
    som.main()

    #som.get_neighbourhood(4, 4)

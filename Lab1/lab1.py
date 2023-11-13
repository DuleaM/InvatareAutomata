import random, math

class GaussAI:
    points_number = 10000
    x_plus = 300
    x_minus = x_plus * -1

    y_plus = 300
    y_minus = y_plus * -1

    zones = [
        {'mx': 180, 'ox': 10, 'my': 220, 'oy': 10, 'color': 'red'},
        {'mx': -100, 'ox': 5, 'my': 50, 'oy': 5, 'color': 'green'},
        {'mx': -200, 'ox': 10, 'my': 100, 'oy': 10, 'color': 'blue'},
        {'mx': -210, 'ox': 5, 'my': -100, 'oy': 5, 'color': 'yellow'},
        {'mx': 150, 'ox': 10, 'my': -150, 'oy': 10, 'color': 'pink'}
    ]

    def __create_file(self):
         file = open("output.txt", "w")
         
         return file
     
    def get_gauss(self, coordinate, zone):
        key = list(coordinate.keys())[0]
        
        numerator = ((zone[f'm{key}'] - coordinate[key]) ** 2)
        denominator = (2 * (zone[f'o{key}'] ** 2))
       
        fraction =  -1 * (numerator / denominator)
        gauss_result = math.e ** fraction
        
        return gauss_result

    def is_valid(self, gauss_value):
        probability = round(random.uniform(0, 1), 4)

        return gauss_value > probability

    #Flush the file every time!
    def main(self):
        count = 0
        file = self.__create_file()

        while count < self.points_number:
            zone_number = random.randint(0, len(self.zones) - 1)
            zone = self.zones[zone_number]

            x_gauss = 0
            y_gauss = 0

            x_coord =  {}
            y_coord = {}

            while not self.is_valid(x_gauss):
                x_coord = {'x': random.randint(self.x_minus, self.x_plus)}
                x_gauss = self.get_gauss(x_coord, zone)

            while not self.is_valid(y_gauss):
                y_coord = {'y': random.randint(self.y_minus, self.y_plus)}
                y_gauss = self.get_gauss(y_coord, zone)

            file.write(f'{x_coord["x"]} {y_coord["y"]} {zone["color"]}\n')
            count += 1

        file.close()

if __name__ == '__main__':
    gauss_ai = GaussAI()
    gauss_ai.main()
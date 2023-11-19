class SOM:
    
    def __init__(self) -> None:
        self.points = self.__get_coordinates()

        
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
        
if __name__ == '__main__':
    som = SOM()
    print(som.points)
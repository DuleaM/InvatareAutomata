import random
import sys
from math import sqrt
from collections import defaultdict
import time


class KMeans():
    
    centroid_number = random.randint(2, 10)
    points = []
    centroids = []
    clusters = {}
    
    def __init__(self):
        self.get_coordinates()
        self.set_centroizi_coordinates()
 

    def get_coordinates(self): 
        with open('output.txt', 'r') as file:
            for line in file:
                elements = line.split()
                x = int(elements[0])
                y = int(elements[1])
                
                coords = {'x' : x, 'y' : y}
                
                self.points.append(coords)
                
                
    def set_centroizi_coordinates(self):
        """
            centroid = {
                number : {
                    'x' : x,
                    'y' : y
                } 
            }
        """
        for centroid_number in range(self.centroid_number):
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            
            coords = {'x' : x, 'y' : y}
            centroid = {centroid_number : coords}
            self.centroids.append(centroid)
    
    
    def get_euclidian_distance(self, point, centroid):
        sum = 0
        for point_coordinate, centroid_coordinate in zip(point.keys(), centroid.keys()):
            sum += (point[point_coordinate] - centroid[centroid_coordinate]) ** 2
            
        euclidian_distance = sqrt(sum)
        
        return round(euclidian_distance)


    def group_points_to_clusters(self):
        """
        cluster = {
            cluster_number : 
            {
                'x' : x,
                'y' : y
            },
            
            {}, etc
        }
        """
        
        clusters = defaultdict(list)
        for point in self.points:
            min_distance = sys.maxsize
            target_centroid = -1
            
            for centroid in self.centroids:
                centroid_number = list(centroid.keys())[0]
                centroid_coords = list(centroid.values())[0]
                
                distance = self.get_euclidian_distance(point, centroid_coords)
                
                if distance < min_distance:
                    min_distance = distance
                    target_centroid = centroid_number 
            
            point['distance'] = min_distance
            clusters[target_centroid].append(point)
        
        return clusters
                
    def get_weight_center(self, cluster):
        
        x_weight_center = 0
        y_weight_center = 0 

        for point in cluster:
            x_weight_center += point['x']
            y_weight_center += point['y']

        x_weight_center /= len(cluster)
        y_weight_center /= len(cluster)
        
        new_centroid = {'x' :round(x_weight_center), 'y' : round(y_weight_center)}
        
        return new_centroid
   
    def modify_centroids_coordinates(self):
        for index, centroid in enumerate(self.centroids):
            cluster = self.clusters[index]
            new_centroid_coordinates = self.get_weight_center(cluster)
            centroid[index] = new_centroid_coordinates
    
    def get_convergenta(self, clusters):
        suma = 0
        for cluster in clusters:
            suma += sum(point for point in cluster)
        
        return suma               
     
    def valid(self, clusters):
        return self.get_convergenta(self.clusters) == self.get_convergenta(clusters)
    
    
    def main(self):
        self.clusters = self.group_points_to_clusters()
        self.modify_centroids_coordinates()
        
        while not self.valid(self.group_points_to_clusters()):
            
            
            self.clusters = self.group_points_to_clusters()
            self.modify_centroids_coordinates()
            

if __name__ == '__main__':
    kmeans = KMeans()
 
    kmeans.main()
    #print(kmeans.clusters)
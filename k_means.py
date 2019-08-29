import math
import random 
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

def kmeans(input_set, k=3, iteration=100):
    init_index = [random.randint(0, len(input_set)-1) for i in range(k)]
    centroids = [input_set[index] for index in init_index]
    labels = [-1 for i in range(len(input_set))]
    
    while(iteration>0):
        clusters = [[] for i in range(k)]        
        for index, data in enumerate(input_set):
            class_id = -1
            dist = math.inf
            for i, centroid in enumerate(centroids):
                d = euclidean_distance(centroid, data)
                if (d < dist):
                    class_id = i
                    dist = d
            clusters[class_id].append(data)
            labels[index] = class_id
        
        for index, cluster in enumerate(clusters):
            new_centroid = [0 for i in range(len(input_set[0]))]
            for member in cluster:
                for i, coordinate in enumerate(member):
                    new_centroid[i] += coordinate/len(cluster)
            centroids[index] = new_centroid
        iteration -= 1

    return centroids, labels


if __name__ == "__main__":
    data = [[1.0, 2.0], [2.0, 3.0], [4.0, 5.0], [4.0, 5.0]]
    c, id = kmeans(data, k = 3, iteration = 100)
    print("Coordinates of each centroids are {}".format(c))
    print("class id of each input are {}".format(id))
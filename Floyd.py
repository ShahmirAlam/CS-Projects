import math


'''
Todo:
Write an algorithm that runs Floyd-Warshall's algorithm on a graph
Input:
M: The adjacency matrix representing the graph
return:
shortest_paths: an array of the n distance matrices on each of the n phases
of the algorithm, where the distance matrix is an n×n matrix whose i-th
row, j-th
column entry denotes the shortest distance from vertex i to vertex j
(at that phase
of the algorithm).
'''
def myFloyd(M):
    n = len(M)
    dist = [M]
    
    # Perform the Floyd-Warshall algorithm
    for k in range(n):
        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = min(dist[k][i][j], dist[k][i][k] + dist[k][k][j])
        dist.append(new_matrix)
    return dist[1:]

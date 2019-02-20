# encoding: utf-8

"""
the first being an adjacency matrix (effective with dense graphs) and second an adjacency list (effective with sparse graphs). 
"""

import numpy as np

class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False
        
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.add_neighbor(neighbor)
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
                
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1])          
    
    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]  
        else:
            return dict()
        
    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(self.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names)))) 
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
            self.adjacency_matrix = np.full(shape=(len(self.vertices),len(self.vertices)), fill_value=99999) # for floyd
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in self.vertices[self.vertex_names[i]]:
                        j = self.vertex_indices[el]
                        self.adjacency_matrix[i,j] = 1 # distance
            return self.adjacency_matrix
        else:
            return dict()              

def floyd(matrix):
    V = len(matrix)
    C = np.zeros(shape=(V, V, V))

    for i in range(V):
        for j in range(V):
            if i != j:
                C[0][i][j] = min(matrix[i][j], matrix[i][0] + matrix[0][j])
            else:
                C[0][i][j] = 0
    print (C)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                C[k][i][j] = min(C[k-1][i][j], C[k-1][i][k] + C[k-1][k][j])

def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())

if __name__ == "__main__": 
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')

    a.add_neighbors([b,c,e]) 
    b.add_neighbors([a,c])
    c.add_neighbors([b,d,a,e])
    d.add_neighbor(c)
    e.add_neighbors([a,c])       
            
    g = Graph()
    g.add_vertices([a,b,c,d,e])
    matrix = g.adjacencyMatrix()
    # print (matrix)
    floyd(matrix)

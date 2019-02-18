# encoding: utf-8

from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

from collections import defaultdict
import heapq

def dijkstra_heapq(graph, initial, target):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}
    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        if min_node == target: 
            return visited, path
        
        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

def dijkstra(graph, start):
  visited = {start: 0}
  path = {}
  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited: 
        if min_node is None:
          min_node = node 
        elif visited[node] < visited[min_node]:
          min_node = node
    
    if min_node is None: 
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for v in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, v)]
      if v not in visited or weight < visited[v]:
        visited[v] = weight
        path[v] = min_node

  return visited, path

if __name__ == "__main__":
    g = Graph()

    g.add_node("1")
    g.add_node("2")
    g.add_node("3")
    g.add_node("4")
    g.add_node("5")
    g.add_node("6")

    g.add_edge("1", "2", 7)
    g.add_edge("1", "6", 14)
    g.add_edge("1", "3", 9)
    g.add_edge("2", "4", 15)
    g.add_edge("3", "4", 11)
    g.add_edge("3", "6", 2)
    g.add_edge("6", "5", 9)
    g.add_edge("4", "5", 6)

    visited, path = dijkstra(g, "1")
    visited, path = dijkstra_heapq(g, "1", "5")
    print (visited, path) # {'1': 0, '3': 9, '2': 7, '5': 20, '4': 20, '6': 11}, {'3': '1', '2': '1', '5': '6', '4': '3', '6': '3'})
    start = "1" 
    end = "5"
    while end != start:
        print (end)
        end = path[end]
    print (end)
    """ 5, 6, 3 , 1 """

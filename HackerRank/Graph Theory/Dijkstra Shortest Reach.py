#!/bin/python
# encoding: utf-8

import math
import os
import random
import re
import sys

from collections import defaultdict
import heapq

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

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    g = Graph()
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])

    h = [(0, s)]
    visited={s:0}
    nodes = set(n+1 for n in range(n))

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        current_weight = visited[min_node]        
        nodes.remove(min_node)

        for node in g.edges[min_node]:
            wt = current_weight + g.distances[(min_node, node)]
            if node not in visited or wt < visited[node]:
                visited[node] = wt
                heapq.heappush(h, (wt, node))
    
    visited_list=[]
    for i in range(n):
        i=i+1
        if i != s:
            if i in visited.keys():
                visited_list.append(visited[i])
            else:
                visited_list.append(-1)
    return visited_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(sys.stdin.readline())
    for t_itr in range(t):
        nm = sys.stdin.readline().split()

        n = int(nm[0])
        m = int(nm[1])
        edges = {}
        for _ in range(m):
            values = list(map(int, sys.stdin.readline().rstrip().split()))
            key = tuple(sorted(values[:2]))
            if key in edges:
                edges[key] = min(values[2], edges[key])
            else:
                edges[key] = values[2]

        edges = [(u, v, r) for (u,v), r in edges.items()]
        s = int(sys.stdin.readline())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

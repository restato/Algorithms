# encoding: utf-8

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in set(graph[n]) - set(path):
                queue.append((m, path + [m]))
    return result

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += set(graph[n]) - set(visited)
    return visited

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

    print (bfs(graph, 'A'))
    print (bfs_paths(graph, 'A', 'F')) 

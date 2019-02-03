#!/bin/python3

import os
import sys

sys.setrecursionlimit(15000)

class Node():
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1

class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.print_list = []

    def in_order(self, node):
        if node == -1:
            return
        self.in_order(node.left)
        if node.data != -1:
            print (node.data)
            self.print_list.append(node.data)
        self.in_order(node.right)
#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    root = Node(1)
    tree = BinaryTree(root)

    nodes = []
    nodes.append(None)
    nodes.append(root)
    nodes_by_depth = {}

    depth = {}
    cur_depth = 1
    depth[nodes[1]] = cur_depth
    nodes_by_depth[cur_depth] = [root]

    for p_index, index in enumerate(indexes):
        l_data, r_data = index[0], index[1]
        p_index += 1 # parent node index start at 0
        # print (p_index, l_data, r_data)
        p_node = nodes[p_index]
        cur_depth = depth[p_node] 

        # l_data 
        if l_data != -1:
            l_node = Node(l_data)
            depth[l_node] = cur_depth + 1
            p_node.left = l_node
            nodes.append(l_node)
            if not cur_depth+1 in nodes_by_depth:
                nodes_by_depth[cur_depth+1] = []
            nodes_by_depth[cur_depth+1].append(l_node)

        if r_data != -1:
            r_node = Node(r_data)
            depth[r_node] = cur_depth + 1
            p_node.right = r_node
            nodes.append(r_node)
            if not cur_depth+1 in nodes_by_depth:
                nodes_by_depth[cur_depth+1] = []
            nodes_by_depth[cur_depth+1].append(r_node)

    height = list(nodes_by_depth.keys())[-1]
    results = []
    for query in queries:
        k = query 
        cur_depth = 1
        while cur_depth != height:
            if cur_depth % k == 0:
                # swap
                # print ("cur_depth:", cur_depth)
                lr_nodes = nodes_by_depth[cur_depth]
                for lr_node in lr_nodes:
                    l = lr_node.left
                    r = lr_node.right
                    lr_node.right = l
                    lr_node.left = r
            cur_depth += 1
        tree.in_order(nodes[1])
        results.append(tree.print_list)
        tree.print_list = []
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

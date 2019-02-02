#!/bin/python3

import os
import sys

class Node:
    def __init__(self): 
        self.child = {}
        self.occur = 1;
    
class Trie:  
    def __init__(self, root):
        self.root = root

    def addNode(self, s):
        cur_node = self.root;
        for char in s:
            if char in cur_node.child.keys():
                cur_node = cur_node.child[char]
                cur_node.occur += 1
            else:
                cur_node.child[char] = Node()
                cur_node = cur_node.child[char]

    def find_partial(self, s):
        cur_node = self.root;
        for char in s:
            if char in cur_node.child.keys():
                cur_node = cur_node.child[char]
            else:
                return 0
        return cur_node.occur 
#
# Complete the contacts function below.
#
def contacts(queries): 
    root = Node()
    trie = Trie(root)
    results = []
    for query in queries:
        op = query[0]
        s  = query[1]
        if op == 'add':
            trie.addNode(s) 
        else: 
            results.append(trie.find_partial(s))
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    
    def level_order_traversal(self, root):
        
        if root == None:
            return
        queues = [deque(), deque()]
        current_queue = queues[0]
        next_queue = queues[1]
        
        current_queue.append(root)
        level_number = 0
        node_dict = {}
        
        while current_queue:
            temp = current_queue.popleft()
            if level_number not in node_dict:
                node_dict[level_number] = []
            node_dict[level_number].append(temp)
            
            if temp.left != None:
                next_queue.append(temp.left)
            if temp.right != None:
                next_queue.append(temp.right) 
                
            if not current_queue:
                level_number += 1
                current_queue = queues[level_number % 2]
                next_queue = queues[(level_number + 1) % 2] 
    
        for nodes in node_dict.values():
            for index in range(len(nodes)-1):
                nodes[index].next = nodes[index+1]            
        return root
            
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.level_order_traversal(root)

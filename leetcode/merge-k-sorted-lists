# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq # heapq min heap based on binary tree
# https://docs.python.org/ko/3/library/heapq.html 
# 구현에서는 모든 k에 대해 heap[k] <= heap[2*k+1]과 heap[k] <= heap[2*k+2]인 배열을 사용합니다

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode(0)
        queue = []
        # it handles the case of a "tie" when two list nodes have the same value. When that happens, Python will look at the next value in the tuple (in this case, count), and sort based on that value. Without count, a "tie" would error out if the next value in the tuple were a ListNode (which can't be compared).
        count = 0 
        
        for l in lists:
            if l is not None:
                count += 1 
                heapq.heappush(queue, (l.val, count, l)) # O(logN)
                
        while len(queue) > 0:
            _, _, curr.next = heapq.heappop(queue) # O(logN)
            curr = curr.next
            if curr.next is not None:
                count += 1
                heapq.heappush(queue, (curr.next.val, count, curr.next))
        return head.next    

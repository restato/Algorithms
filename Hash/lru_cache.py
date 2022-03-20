# https://leetcode.com/problems/lru-cache

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

# LRU (Least Recently Used): 가장 최근에 적게 사용한 녀석을 지운다 (=최근 사용한 애를 항상 뒤로)
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail # 🔑
        self.tail.prev = self.head # 🔑

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            # 최근 사용한 노드는 항상 마지막으로
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        # 있으면 지우고 다시 추가 (맨 마지막으로 이동)
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        # capa 가 넘으면 맨 앞을 제거
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # double-linked list의 마지막에 추가
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# encoding: utf-8
#! usr/bin/python

class Heap(object):
    def __init__(self):
        print ("Min Heap")
        self.array = []

    def find_parent(self, index):
        if index == 0:
            return -1
        if index % 2 == 0:
            return (index-2)/2
        return (index-1)/2

    def insert(self, value):
        self.array.append(value)
        parent_index = self.find_parent(len(self.array) - 1)

        if parent_index != -1:
            print (self.array[parent_index], value)
            if self.array[parent_index] > value:
                self.up(len(self.array)-1, parent_index)

    # up 에서는 부모보다 값이 더 큰 녀석을 위쪽으로 올려 줘야 한다.
    def up(self, c, t):  # c = current_index, t = target_index
        self.array[c], self.array[t] = self.array[t], self.array[c]
        c = t
        while True:
            parent_index = self.find_parent(c)
            if parent_index == -1: # 최상위 노드라면 업데이트 필요 없음
                break
            if self.array[parent_index] < self.array[c]:
                break
            t = parent_index # 부모의 노드를 계속 업데이트

            self.array[c], self.array[t] = self.array[t], self.array[c]
            c = t

    def find_child(self, index):
        left_child  = (index*2) + 1
        right_child = (index*2) + 2

        if left_child >= len(self.array) and right_child >= len(self.array):
            return -1
        if left_child >= len(self.array):
            return right_child
        if right_child >= len(self.array):
            return left_child

        return left_child if self.array[left_child] < self.array[right_child] else right_child

    def pop(self):
        pop_value = self.array[0]
        self.array[0] = self.array.pop()
        n_i = 0
        while True:
            r_i = self.find_child(n_i)
            if r_i == -1:
                break
            if self.array[n_i] < self.array[r_i]:
                self.array[n_i], self.array[r_i] = self.array[r_i], self.array[n_i]
                n_i = r_i
            else:
                break
        return pop_value

input = [12,4,5,3,8,7,1]

heap = Heap()
for number in input:
    heap.insert(number)

print (heap.array)
print (heap.pop())

#!/bin/python3

import os
import sys

class Min_Heap(object):
    def __init__(self):
        self.array = []

    def find_parent(self, index):
        if index == 0:
            return -1
        if index % 2 == 0:
            return int((index-2)/2)
        return int((index-1)/2)

    def insert(self, value):
        self.array.append(value)
        parent_index = self.find_parent(len(self.array) - 1) 
        if parent_index != -1:
            if self.array[parent_index] > value:
                self.up(len(self.array)-1, parent_index)

    def up(self, c, t):
        self.array[c], self.array[t] = self.array[t], self.array[c]
        c = t
        while True:
            parent_index = self.find_parent(c)
            if parent_index == -1:
                break
            if self.array[parent_index] < self.array[c]:
                break
            t = parent_index

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
            if self.array[n_i] > self.array[r_i]:
                self.array[n_i], self.array[r_i] = self.array[r_i], self.array[n_i]
                n_i = r_i
            else:
                break
        return pop_value


class Max_Heap(object):
    def __init__(self):
        self.array = []

    def find_parent(self, index):
        if index == 0:
            return -1
        if index % 2 == 0:
            return int((index-2)/2)
        return int((index-1)/2)

    def insert(self, value):
        self.array.append(value)
        parent_index = self.find_parent(len(self.array) - 1)

        if parent_index != -1:
            if self.array[parent_index] < value:
                self.up(len(self.array)-1, parent_index)

    def up(self, c, t):
        self.array[c], self.array[t] = self.array[t], self.array[c]
        c = t
        while True:
            parent_index = self.find_parent(c)
            if parent_index == -1:
                break
            if self.array[parent_index] > self.array[c]:
                break
            t = parent_index

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

        return left_child if self.array[left_child] > self.array[right_child] else right_child

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

def median(lower, upper):
    if len(lower) == len(upper):
        return (float(lower[0]) + float(upper[0]))/2.0
    elif len(lower) > len(upper):
        return float(lower[0])
    else:
        return float(upper[0])

def balance(min_heap, max_heap):
    lower = min_heap.array
    upper = max_heap.array
    if abs(len(upper) - len(lower)) >= 2:
        if len(lower) < len(upper):
            min_heap.insert(max_heap.pop())
        else:
            max_heap.insert(min_heap.pop())

#
# Complete the runningMedian function below.
#


def runningMedian(a):
    result = []

    min_heap = Min_Heap() 
    max_heap = Max_Heap()
    
    for value in a:
        print (value)
        if (len(max_heap.array) == 0) or (value < max_heap.array[0]):
            max_heap.insert(value)
        else:
            min_heap.insert(value)
        balance(min_heap, max_heap)
        result.append(median(min_heap.array, max_heap.array))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

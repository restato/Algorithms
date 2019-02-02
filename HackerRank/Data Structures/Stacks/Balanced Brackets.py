#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below. 
def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"  
    
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    stack = []

    for letter in s:
        if letter in opening:
            stack.append(mapping[letter])
        elif letter in closing:
            if len(stack) is 0 or letter != stack.pop():
                return "NO"
    return "YES" 
    
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

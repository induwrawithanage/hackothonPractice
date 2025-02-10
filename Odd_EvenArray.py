#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#
def find(x,y,arr):
    if (x > y):
        return 1
    ans = arr[x]**find(x+1,y,arr)
    return ans


def solve(arr, queries):
    result = []
    size = len(queries)
    for i in range(size):
        x = queries[i][0]
        y = queries[i][1]
        if (find(x,y,arr) % 2 == 0):
            result.append("Even")
        else:
            result.append("Odd")
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

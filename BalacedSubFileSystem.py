#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    from collections import defaultdict
    tree = defaultdict(list)
    for child, par in enumerate(parent):
        if par != -1:
            tree[par].append(child)
    n = len(parent)
    subtree_sums = [0] * n
    total_size = sum(files_size)
    def dfs(node):
        subtree_sums[node] = files_size[node] 
        for child in tree[node]:
            subtree_sums[node] += dfs(child)  
        return subtree_sums[node]

    dfs(0)  
    min_difference = float('inf')
    for i in range(1, n):  
        diff = abs(total_size - 2 * subtree_sums[i])
        min_difference = min(min_difference, diff)

    return min_difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()

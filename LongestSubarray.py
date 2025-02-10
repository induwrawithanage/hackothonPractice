#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
        
def longestSubarray(arr):
    left = 0
    max_length = 0
    count = {}  
    for right in range(len(arr)):
        count[arr[right]] = count.get(arr[right], 0) + 1
        while len(count) > 2 or (max(count) - min(count) > 1):
            count[arr[left]] -=1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left +=1  
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

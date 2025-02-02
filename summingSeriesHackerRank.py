#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):
    return (n * n) % (10**9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()


# this problem is a simple math problem. The sum of the series is n^2.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    diff_all = []
    pairs = []
    
    _arr = sorted(arr)
    
    for i in range(len(_arr) - 1):
        diff_all.append(_arr[i + 1] - _arr[i])
    
    min_diff = min(diff_all)
    
    for i in range(len(diff_all)):
        if diff_all[i] == min_diff:
            pairs.append(_arr[i])
            pairs.append(_arr[i + 1])
    
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

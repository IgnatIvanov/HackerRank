#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    subseq = 0
    subarr = 0
    
    for num in arr:
        if num > 0:
            subseq += num
    
    _max = max(arr)
    s_arr = []
    current = 0
    if _max < 0:
        subseq = _max
        subarr = _max
    else:
        for num in arr:
            if num >= 0:
                current += num
            else:
                s_arr.append(current)
                current = 0
                
        if current > 0:
            s_arr.append(current)
        subarr = max(s_arr)  
        
    max_sum = [arr[0]]
    for i in range(1, len(arr)):
        max_sum.append(max(max_sum[i - 1] + arr[i], arr[i]))
        
    subarr = max(max_sum)
                
    return [subarr, subseq]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    if len(arr) == 1:
        return 'YES'
    
    if len(arr) == 2:
        if arr[0] == 0 or arr[1] == 0:
            return 'YES'
            
    if sum(arr[1:]) == 0 or sum(arr[:-1]) == 0:
        return 'YES'   
    
    left = arr.pop(0)
    right = arr.pop(-1)
    while len(arr) != 1:
        if left > right:
            right += arr.pop(-1)
        elif left < right:
            left += arr.pop(0)
        elif left == right:
            if len(arr) == 1:
                return 'YES' 
            
            if len(arr) == 2:
                if arr[0] == 0 or arr[1] == 0:
                    return 'YES'
                
            if sum(arr[1:]) == 0 or sum(arr[:-1]) == 0:
                return 'YES'
            
            left += arr.pop(0)
            right += arr.pop(-1)
            continue
        
            
    if left == right:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

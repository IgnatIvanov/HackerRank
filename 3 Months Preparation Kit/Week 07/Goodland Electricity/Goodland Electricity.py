#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    n = 0
    last_pylon = k * -1
    
    ##  Installing first pylon
    i = k - 1
    while i > -1:
        if arr[i] == 0:
            i -= 1
        else:
            last_pylon = i
            n += 1
            break
        
    next_pylon = last_pylon + ((k - 1) * 2) + 1
    
    #sums = []
    #for i in range(len(arr) - k + 1):
        #sums.append(sum(arr[i:i+k+k-1]))
    #if 0 in sums:
        #return -1
    
    while True:
        for i in reversed(range(last_pylon, next_pylon + 1)):
            #if i >= len(arr):
                #continue
            #if i < 0:
                #return -1
            if i == last_pylon:
                return -1
            if arr[i] == 1:
                last_pylon = i
                n += 1
                next_pylon = last_pylon + ((k - 1) * 2) + 1
                break
        
        if last_pylon + k >= len(arr):
            return n
        elif last_pylon + 2 * k + 1 >= len(arr):
            next_pylon = len(arr) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

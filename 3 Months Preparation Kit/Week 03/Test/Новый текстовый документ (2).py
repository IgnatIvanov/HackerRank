#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    factors_b = []
    max_mul = 1
    for number in a:
        max_mul = max_mul * number
    for number in b:
        for i in range(1, min(b) + 1):
            if number % i == 0:
                if i not in factors_b:
                    factors_b.append(i)
                    
    factors_b = sorted(factors_b)
    
    #return factors_b
    
    for number in a:
        current = 0
        while current < len(factors_b):
            if factors_b[current] % number != 0:
                factors_b.pop(current)
                continue
            else:
                current += 1
                
    for number in factors_b:
        for i in range(len(b)):
            if  b[i] % number != 0:
                try:
                    factors_b.remove(number)
                except ValueError:
                    pass
                
    #for number in b:
        #if number in factors_b:
            #factors_b.remove(number)
    
    return len(factors_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

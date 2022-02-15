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
    for number in b:
        for i in range(1, number + 1):
            if number % i == 0:
                if i not in factors_b:
                    factors_b.append(i)
                    
    factors_b = sorted(factors_b)    
    print(factors_b)
    
    for number in a:
        current = 0
        while current < len(factors_b):
            if factors_b[current] % number != 0:
                factors_b.pop(current)
                continue
            else:
                current += 1
                
    print(factors_b)
    
    for number in b:
        current = 0
        while current < len(factors_b):
            if number % factors_b[current] != 0:
                factors_b.pop(current)
                continue
            else:
                current += 1
    
    print(factors_b)
    
    return len(factors_b)

if __name__ == '__main__':
    arr = [2, 4]

    brr = [16, 32, 96]

    print(getTotalX(arr, brr))
